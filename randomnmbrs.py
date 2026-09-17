import random

numbers = [random.randint(1, 50) for _ in range(10)]

print("Die zufällig generierten Zahlen sind:", numbers)
print("Die kleinste Zahl ist:", min(numbers))
print("Die größte Zahl ist:", max(numbers))
print("Die Summe der Zahlen ist:", sum(numbers))
print("Der Durchschnitt der Zahlen ist:", sum(numbers) / len(numbers))
print("Die Zahlen in aufsteigender Reihenfolge:", sorted(numbers))
print("Die Zahlen in absteigender Reihenfolge:", sorted(numbers, reverse=True))
print("Die Zahlen ohne Duplikate:", list(set(numbers)))
print("Die Anzahl der Zahlen ist:", len(numbers))
print("Die Anzahl der geraden Zahlen ist:", len([num for num in numbers if num % 2 == 0]))
print("Die Anzahl der ungeraden Zahlen ist:", len([num for num in numbers if num % 2 != 0]))
print("Die Anzahl der Primzahlen ist:", len([num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]))
print("Die Anzahl der Zahlen größer als 25 ist:", len([num for num in numbers if num > 25]))
print("Die Anzahl der Zahlen kleiner als 25 ist:", len([num for num in numbers if num < 25]))