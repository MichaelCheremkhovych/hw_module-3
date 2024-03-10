import re #актувуємо модуль

def normalize_phone(phone_number): #створюємо функцію
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number) #видаляємо всі символи, крім цифр та '+'

    if not cleaned_number.startswith('+'): #перевіряємо чи не починається з '+' та робимо виправлєння префікса
        if not cleaned_number.startswith('38'): #перевіряємо чи не містить міжнародний код, додаємо код '+38' для номерів з України
            cleaned_number = '+38' + cleaned_number
        else:
            cleaned_number = '+' + cleaned_number

    return cleaned_number

#приклад з використання:
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for number in phone_numbers:
    normalized_number = normalize_phone(number)
    print(f"Вхідний номер: {number}, Нормалізований номер: {normalized_number}")
