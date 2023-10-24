from datetime import date, datetime
user_week = {'Monday': [], 
             'Tuesday': [], 
             'Wednesday': [], 
             'Thursday': [], 
             'Friday': [], 
             'Saturday': [],
             'Sunday': [],
             }

def get_birthdays_per_week(users):
    date_now = datetime.now().date()
    day_now = date_now.weekday()
    print(day_now)
    for day in range(day_now, 6):
        print(day)
        if day == 0:
            

    # Реалізуйте тут домашнє завдання
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Grot", "birthday": datetime(1957, 2, 1).date()},
        {"name": "Jan Swift", "birthday": datetime(1977, 12, 5).date()},
        {"name": "Jan Forest", "birthday": datetime(1978, 12, 5).date()},
        {"name": "Jan Tard", "birthday": datetime(1980, 11, 3).date()},
        {"name": "Jan Weis", "birthday": datetime(1990, 11, 4).date()},
        {"name": "Jan Flint", "birthday": datetime(1972, 10, 31).date()},
        {"name": "Jan Boss", "birthday": datetime(1976, 10, 30).date()},
        {"name": "Jan Grape", "birthday": datetime(1977, 11, 1).date()},
        {"name": "Jan Bad", "birthday": datetime(1977, 11, 5).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
