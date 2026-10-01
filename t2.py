from PIL import Image

def swap_left_right(originalbild):
    breite, hoehe = originalbild.size
    pixel = originalbild.load()
    neues_bild = Image.new("RGB", (breite, hoehe))
    neues_pixel = neues_bild.load()

    mitte_x = breite // 2

    for x in range(breite):
        for y in range(hoehe):
            if x < mitte_x:
                neues_pixel[x + (breite - mitte_x), y] = pixel[x, y]
            else:
                neues_pixel[x - mitte_x, y] = pixel[x, y]

    return neues_bild

originalbild = Image.open("bild.jpg")
getauscht = swap_left_right(originalbild)
getauscht.save("getauscht_horizontal.png")