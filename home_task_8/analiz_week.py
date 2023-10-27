# Аналіз місячної чистоти тижня щодо тих дат, які запропоновано, без врахування року на стикові місяців
from datetime import date, datetime


users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 1).date()},
        {"name": "Jan Grot", "birthday": datetime(1957, 2, 1).date()},
        {"name": "Jan Swift", "birthday": datetime(1977, 2, 5).date()},
        {"name": "Jan Forest", "birthday": datetime(1978, 2, 5).date()},
        {"name": "Jan Tard", "birthday": datetime(1980, 10, 14).date()},
        {"name": "Jan Weis", "birthday": datetime(1972, 10, 15).date()},
        {"name": "Jan Flint", "birthday": datetime(1972, 10, 16).date()},
        {"name": "Jan Boss", "birthday": datetime(1972, 10, 22).date()},
        {"name": "Jan Grape", "birthday": datetime(1972, 10, 27).date()},
        {"name": "Jan Bad", "birthday": datetime(1977, 10, 18).date()},
    ]


date_now = datetime(year=2022, month=10, day=30)
    #date_now = datetime.now().date()
    #date_now = date.today()
    #print(date_now)
day_now = date_now.weekday()
    #print(day_now)
day_now_word = date_now.strftime("%A")
month = date_now.strftime("%m")
date_ = date_now.strftime("%d")


for dict in users:
    for value in dict.values():
        pass
    #print(value)
    
    analiz_month = value.month - month
    if analiz_month == 1:
        
    

    # same_day = value.day
    # same_month = value.month
    # now_year = year=2023
    # actual_datetime = datetime(now_year, same_month, same_day).date()

    # #print(actual_datetime) 
    # weekday_ = actual_datetime.weekday()
    # print(weekday_)
