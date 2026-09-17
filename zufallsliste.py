import random

zahlen = []

for i in range(10):
    zufallszahl = random.randint(1, 100)
    zahlen.append(zufallszahl)

print(zahlen)

def durchschnitt(zahlen):
    if len(zahlen) == 0:
        return 0

    return sum(zahlen) / len(zahlen)

x = int(input("Möchtest du den Durchschnitt deiner Liste berechnen? (1 für Ja, 0 für Nein): "))
if x == 1:
    print("Durchschnitt deiner Liste:", durchschnitt(zahlen))