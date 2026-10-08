from PIL import Image

def drehe_links(originalbild):
    breite, hoehe = originalbild.size
    pixel = originalbild.load()

    neues_bild = Image.new("RGB", (hoehe, breite))
    neues_pixel = neues_bild.load()

    for x in range(breite):
        for y in range(hoehe):
            neues_pixel[hoehe - 1 - y, x] = pixel[x, y]

    return neues_bild

originalbild = Image.open("bild.jpg")
gedreht = drehe_links(originalbild)
gedreht = drehe_links(gedreht)
gedreht = drehe_links(gedreht)
gedreht.save("gedreht_links.png")