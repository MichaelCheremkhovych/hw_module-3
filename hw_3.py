from datetime import datetime #Імпортуємо дані з модулю datetime

def get_days_from_today(date): #Створюємо функцію get_days_from_today тільки для одного параметра date
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d") #Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД'

        current_date = datetime.today() #Отримуємо поточну дату
        
        date_difference = current_date - input_date #Розраховуємо різницю між поточною датою та заданою датою
               
        return date_difference.days #Повертаємо різницю у днях як ціле число

    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.") #Обробка винятка для невірного формату даних
        return None

#Приклад використання для сьогоднішньої дати 9 березня 2024
today = "2024-03-09"  
result = get_days_from_today("2021-10-09")

#Виводимо результат з даними з приклада
if result is not None:
    print(f"Різниця в днях між {today} та '2021-10-09': {result}")
