from PIL import Image

def kolorieren(pfad):
    bild = Image.open(pfad).convert("RGB")
    pixel = bild.load()

    breite, hoehe = bild.size

    for x in range(breite):
        for y in range(hoehe):
            r, g, b = pixel[x, y]
            grau = (r + g + b) // 3

            if grau < 12:
                farbe = (12, 12, 16)
            elif grau < 24:
                farbe = (25, 20, 35)
            elif grau < 36:
                farbe = (38, 28, 48)
            elif grau < 48:
                farbe = (48, 35, 60)
            elif grau < 60:
                farbe = (55, 45, 75)
            elif grau < 72:
                farbe = (50, 60, 90)
            elif grau < 84:
                farbe = (45, 75, 100)
            elif grau < 96:
                farbe = (45, 95, 105)
            elif grau < 108:
                farbe = (50, 110, 95)
            elif grau < 120:
                farbe = (65, 125, 80)
            elif grau < 132:
                farbe = (100, 140, 70)
            elif grau < 144:
                farbe = (145, 150, 65)
            elif grau < 156:
                farbe = (180, 145, 65)
            elif grau < 168:
                farbe = (195, 125, 75)
            elif grau < 180:
                farbe = (195, 105, 95)
            elif grau < 192:
                farbe = (200, 135, 130)
            elif grau < 204:
                farbe = (210, 165, 160)
            elif grau < 216:
                farbe = (220, 195, 190)
            elif grau < 235:
                farbe = (235, 230, 225)
            else:
                farbe = (255, 255, 255)

            pixel[x, y] = farbe

    bild.save("chati.png")
    return bild


kolorieren("schwarzweiss.png")