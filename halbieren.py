from PIL import Image

def halbieren(originalbild):
    breite, hoehe = originalbild.size
    pixel = originalbild.load()

    neues_bild = Image.new("RGB", (breite // 2, hoehe // 2))
    neues_pixel = neues_bild.load()
    for x in range(breite // 2):
        for y in range(hoehe // 2):
            neues_pixel[x, y] = pixel[x, y]

    return neues_bild
originalbild = Image.open("bild.jpg")
halbiertes_bild = halbieren(originalbild)
halbiertes_bild.save("halbiert.png")