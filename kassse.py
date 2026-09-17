alter = int(input("Wie alt bist du? "))

if alter < 6:
    preis = 0
elif alter >= 65:
    preis = 15
elif alter >= 18:
    preis = 20
else:
    preis = 10

schuelerkarte = input("Hast du eine Schülerkarte? (ja/nein) ")

if schuelerkarte == "ja":
    preis = max(0, preis - 5)

print("Der Eintritt kostet", preis, "Euro.")
