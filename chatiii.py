import numpy as np
import torch
from PIL import Image
from scipy.ndimage import gaussian_filter
from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation

# pip install torch transformers scipy numpy pillow

# --- 1) Grundfärbung nach Grauwert (wie vorher) ---
STUETZPUNKTE = [
    (0,   165, 90), (50, 160, 70), (95, 130, 35),
    (130,  18, 55), (170, 22, 60), (215, 30, 30), (255, 0, 0),
]

# --- 2) Natürliche Farbrampen: (Grauwert, (R, G, B)) ---
ROT = [
    (0,   (20, 0, 0)),
    (50,  (95, 3, 8)),        # tiefes Weinrot
    (110, (175, 10, 15)),     # klassisches Rücklichtrot
    (170, (225, 35, 30)),     # leuchtendes Rot
    (220, (255, 140, 120)),   # rosa-heller Rand
    (255, (255, 255, 255)),   # Reflexe bleiben weiß
]

# --- 3) Was soll automatisch gefunden und gefärbt werden? ---
OBJEKTE = [
    {"text": "car taillight", "rampe": ROT, "schwelle": 0.35},
]

processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
modell = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")

def grundfaerbung(grau):
    a = np.array(grau)
    g = np.arange(256)
    xs, hs, ss = zip(*STUETZPUNKTE)
    hue = np.interp(g, xs, hs).astype(np.uint8)[a]
    sat = np.interp(g, xs, ss).astype(np.uint8)[a]
    hsv = np.stack([hue, sat, a], axis=-1)
    return np.array(Image.fromarray(hsv, "HSV").convert("RGB")).astype(float)

def rampe_anwenden(a, rampe):
    xs = [p[0] for p in rampe]
    return np.stack(
        [np.interp(a, xs, [p[1][k] for p in rampe]) for k in range(3)], axis=-1
    )

def maske_finden(rgb_bild, text, schwelle):
    inputs = processor(text=[text], images=[rgb_bild], return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = modell(**inputs).logits
    m = torch.sigmoid(logits).reshape(logits.shape[-2], logits.shape[-1]).numpy()
    m = np.array(Image.fromarray((m * 255).astype(np.uint8)).resize(rgb_bild.size, Image.BICUBIC)) / 255.0
    m = np.clip((m - schwelle) / (1 - schwelle), 0, 1)   # weicher Übergang
    return gaussian_filter(m, 2)

def kolorieren(pfad, ausgabe="farbig.png"):
    original = Image.open(pfad).convert("RGB")
    grau = original.convert("L")
    a = np.array(grau)
    ergebnis = grundfaerbung(grau)

    for o in OBJEKTE:
        m = maske_finden(original, o["text"], o["schwelle"])[..., None]
        objekt = rampe_anwenden(a, o["rampe"])
        ergebnis = ergebnis * (1 - m) + objekt * m

    Image.fromarray(np.clip(ergebnis, 0, 255).astype(np.uint8)).save(ausgabe)

kolorieren("schwarzweiss.png")