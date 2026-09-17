def durchschnitt(zahlen):
    if len(zahlen) == 0:
        return 0

    return sum(zahlen) / len(zahlen)


liste1 = [2, 4, 6, 8]
liste2 = [10, 20, 30]
liste3 = [5]

print("Durchschnitt von liste1:", durchschnitt(liste1))
print("Durchschnitt von liste2:", durchschnitt(liste2))
print("Durchschnitt von liste3:", durchschnitt(liste3))
