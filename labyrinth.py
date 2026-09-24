def finde_position(labyrinth, gesucht):
    """Findet die Position eines bestimmten Zeichens."""
    for zeile in range(len(labyrinth)):
        for spalte in range(len(labyrinth[zeile])):
            if labyrinth[zeile][spalte] == gesucht:
                return zeile, spalte

    return None


def finde_weg(labyrinth):
    start = finde_position(labyrinth, "S")
    ziel = finde_position(labyrinth, "Z")

    if start is None or ziel is None:
        return False, 0

    # Warteschlange für die Breitensuche
    warteschlange = [start]

    # Felder, die bereits untersucht wurden
    besucht = [start]

    # Für jedes Feld wird sein Vorgänger gespeichert
    vorgaenger = {}

    # Bewegungen: oben, unten, links, rechts
    bewegungen = [
        (-1, 0),  # oben
        (1, 0),   # unten
        (0, -1),  # links
        (0, 1)    # rechts
    ]

    while warteschlange:
        aktuelle_position = warteschlange.pop(0)

        if aktuelle_position == ziel:
            break

        aktuelle_zeile, aktuelle_spalte = aktuelle_position

        for bewegung_zeile, bewegung_spalte in bewegungen:
            neue_zeile = aktuelle_zeile + bewegung_zeile
            neue_spalte = aktuelle_spalte + bewegung_spalte
            neue_position = (neue_zeile, neue_spalte)

            # Prüfen, ob die neue Position innerhalb des Labyrinths liegt
            if not (0 <= neue_zeile < len(labyrinth)):
                continue

            if not (0 <= neue_spalte < len(labyrinth[neue_zeile])):
                continue

            # Nur freie und noch nicht besuchte Felder betreten
            if labyrinth[neue_zeile][neue_spalte] == "#":
                continue

            if neue_position in besucht:
                continue

            besucht.append(neue_position)
            warteschlange.append(neue_position)
            vorgaenger[neue_position] = aktuelle_position

    # Wurde das Ziel nicht erreicht?
    if ziel not in besucht:
        return False, 0

    # Weg vom Ziel zurück zum Start verfolgen
    weg = []
    position = ziel

    while position != start:
        weg.append(position)
        position = vorgaenger[position]

    weg.append(start)
    weg.reverse()

    # Weg markieren, aber Start und Ziel nicht überschreiben
    for zeile, spalte in weg:
        if labyrinth[zeile][spalte] not in ("S", "Z"):
            labyrinth[zeile][spalte] = "*"

    # Anzahl der Schritte:
    # Anzahl der Wegfelder minus Startfeld
    schritte = len(weg) - 1

    return True, schritte


def drucke_labyrinth(labyrinth):
    for zeile in labyrinth:
        print(" ".join(zeile))


labyrinth = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "S", ".", ".", "#", "#"],
    ["#", "#", ".", ".", ".", "#"],
    ["#", ".", ".", "#", ".", "#"],
    ["#", ".", "#", ".", "Z", "#"],
    ["#", "#", "#", "#", "#", "#"]
]

gefunden, schritte = finde_weg(labyrinth)

if gefunden:
    print("Weg gefunden:")
    drucke_labyrinth(labyrinth)
    print("Schritte:", schritte)
else:
    print("Es gibt keinen Weg zum Ziel.")