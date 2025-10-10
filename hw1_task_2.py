import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6)) # 6 випадкових чисел 1–49
print(get_numbers_ticket(10, 20, 5)) # діапазон 10–20
print(get_numbers_ticket(1, 1000, 10)) # усе валідно
print(get_numbers_ticket(1, 10, 0)) # quantity = 0
print(get_numbers_ticket(5, 5, 1)) # некоректний діапазон
