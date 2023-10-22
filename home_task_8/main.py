from datetime import date, datetime


def get_birthdays_per_week(users):
    

    # Реалізуйте тут домашнє завдання
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Grot", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Swift", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Forest", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Tard", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Weis", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Flint", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Boss", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Grape", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Bad", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
