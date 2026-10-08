from PIL import Image

def schwarzweiss(originalbild):
    breite, hoehe = originalbild.size
    pixel = originalbild.load()

    neues_bild = Image.new("L", (breite, hoehe))
    neues_pixel = neues_bild.load()

    for x in range(breite):
        for y in range(hoehe):
            neue_helligkeit = min(1000, pixel[x, y][0] + pixel[x, y][1] + pixel[x, y][2]) // 3
            neues_pixel[x, y] = neue_helligkeit

    return neues_bild

originalbild = Image.open("bild.jpg")
schwarzweiss_bild = schwarzweiss(originalbild)
schwarzweiss_bild.save("schwarzweiss.png")