import random #активуємо модуль random

def get_numbers_ticket(minimum, maximum, quantity): #створюємо функцію
    #перевірка коректності вхідних параметрів
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return []

    #генерація унікальних випадкових чисел
    numbers_set = set()
    while len(numbers_set) < quantity: #за допомогою цикла зрівнюємо 
        numbers_set.add(random.randint(minimum, maximum))

    #повертаємо відсортований список
    return sorted(list(numbers_set))

#приклад
minimum_number = 1
maximum_number = 49
quantity_to_select = 6

result = get_numbers_ticket(minimum_number, maximum_number, quantity_to_select)
print(f"Ваш лотерейний квиток: {result}")
