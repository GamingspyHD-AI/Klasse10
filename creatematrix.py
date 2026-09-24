
ZEILEN = 5
SPALTEN = 5
ZAHL = 6

matrix = []

for zeile in range(ZEILEN):
    neue_zeile = []

    for spalte in range(SPALTEN):
        neue_zeile.append(ZAHL)

    matrix.append(neue_zeile)

print(matrix)