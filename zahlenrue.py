a = int(input("Gib eine 1 oder 2 ein: "))
if a == 1:
    x = 20
    while x >= 0:
        print(x)
        x -= 1

elif a == 2:
    y = 0
    while y <= 30:
        print(y)
        y += 3

else:
    print("Ungültige Eingabe. Bitte gib 1 oder 2 ein.")