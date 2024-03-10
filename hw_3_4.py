from datetime import datetime, timedelta #імпортуємо з модуля datetime інструменти datetime та timedelta

def find_next_weekday(d, weekday: int):
    
    #функція для знаходження наступного заданого дня тижня після заданої дати
    #параметр d: datetime.date - початкова дата
    #параметр weekday типу int - день тижня від 0 (понеділок) до 6 (неділя)
    
    
    days_ahead = weekday - d.weekday()  #різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  #якщо день народження вже минув
        days_ahead += 7  #додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  #повертаємо нову дату

def prepare_users(users):
    
    #Функція для підготовки користувачів, конвертує дату народження в об'єкт datetime.date
    #парамерт users: list - список користувачів
    
    
    prepared_users = [] #список підготовлених користувачів

    for user in users: #ітерація по кожному користувачеві зі списку
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date() #парсимо дату народження
            prepared_users.append({"name": user['name'], 'birthday': birthday}) #додаємо користувача з підготовленою датою народження
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}') #виводимо повідомлення про помилку

    return prepared_users #повертаємо список підготовлених користувачів

def get_upcoming_birthdays(prepared_users, days=7):
    
    #функція для знаходження майбутніх днів народження користувачів
    #параметр prepared_users: list - список підготовлених користувачів
    #параметр days: int - кількість днів для перевірки на наближені дні народження
    
    
    today = datetime.today().date() #поточна дата
    upcoming_birthdays = [] #список майбутніх днів народження

    for user in prepared_users: #ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year) #заміна року на поточний для дня народження цього року

        if birthday_this_year < today: #якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) #переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= days: #якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5: #якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0) #знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d') #форматуємо дату у рядок
            upcoming_birthdays.append({                           #додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays #повертаємо список словників із даними про майбутні дні народження

# Приклад використання функцій
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Jane Smith1", "birthday": "1990.03.12"},
    {"name": "Jane Smith1", "birthday": "1990.03.08"},
]

# Підготувати користувачів
prepared_users = prepare_users(users)

# Знайти майбутні дні народження
upcoming_birthdays = get_upcoming_birthdays(prepared_users)
print("Список майбутніх днів народження:", upcoming_birthdays) #виводимо список майбутніх днів народження
