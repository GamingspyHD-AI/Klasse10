SIZE = 2
ZAHL = 6

matrix = []

for zeile in range(SIZE):
    neue_zeile = []

    for spalte in range(SIZE):
        neue_zeile.append(ZAHL)

    matrix.append(neue_zeile)

for element in matrix:
    print(element)
