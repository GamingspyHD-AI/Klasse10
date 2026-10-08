from PIL import Image

def negativ(originalbild):
    breite, hoehe = originalbild.size
    pixel = originalbild.load()

    neues_bild = Image.new("RGB", (breite, hoehe))
    neues_pixel = neues_bild.load()

    for x in range(breite):
        for y in range(hoehe):
            neues_pixel[x, y] = (255 - pixel[x, y][0], 255 - pixel[x, y][1], 255 - pixel[x, y][2])

    return neues_bild
originalbild = Image.open("bild.jpg")
negativ_bild = negativ(originalbild)
negativ_bild.save("negativ.png")