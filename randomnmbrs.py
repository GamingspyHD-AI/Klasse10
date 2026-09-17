import random

numbers = [random.randint(1, 50) for _ in range(10)]

print("Die zufällig generierten Zahlen sind:", numbers)
print("Die kleinste Zahl ist:", min(numbers))
print("Die größte Zahl ist:", max(numbers))
print("Die Summe der Zahlen ist:", sum(numbers))
print("Der Durchschnitt der Zahlen ist:", sum(numbers) / len(numbers))
