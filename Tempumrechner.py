def celsius_zu_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def drucke_umrechnung(t1, t2):
    for celsius in range(t1, t2 + 1):
        fahrenheit = celsius_zu_fahrenheit(celsius)
        print(celsius, "°C =", fahrenheit, "°F")


x = int(input("Gib die untere Temperaturgrenze in °C ein: "))
y = int(input("Gib die obere Temperaturgrenze in °C ein: "))
drucke_umrechnung(x, y)
