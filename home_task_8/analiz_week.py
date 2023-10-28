# Аналіз місячної чистоти тижня щодо тих дат, які запропоновано, без врахування року на стикові місяців
from datetime import date, datetime


users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 1).date()},
        {"name": "Jan Grot", "birthday": datetime(1957, 2, 1).date()},
        {"name": "Jan Swift", "birthday": datetime(1977, 2, 5).date()},
        {"name": "Jan Forest", "birthday": datetime(1978, 2, 5).date()},
        {"name": "Jan Tard", "birthday": datetime(1980, 10, 2).date()},
        {"name": "Jan Weis", "birthday": datetime(1972, 10, 15).date()},
        {"name": "Jan Flint", "birthday": datetime(1972, 10, 16).date()},
        {"name": "Jan Boss", "birthday": datetime(1972, 10, 22).date()},
        {"name": "Jan Grape", "birthday": datetime(1972, 10, 27).date()},
        {"name": "Jan Bad", "birthday": datetime(1977, 10, 18).date()},
    ]


date_now = datetime(year=2023, month=10, day=2)
    #date_now = datetime.now().date()
    #date_now = date.today()
    #print(date_now)
#day_now = date_now.weekday()
    #print(day_now)
#day_now_word = date_now.strftime("%A")
month = date_now.strftime("%m")
#date_ = date_now.strftime("%d")


for dict in users:
    for value in dict.values():
        pass
    #print(value)
    same_day = value.day
    same_month = value.month
    now_year = year=2023
    actual_datetime = datetime(now_year, same_month, same_day).date()

    #print(actual_datetime) 
    #weekday_ = actual_datetime.weekday()
    #print(weekday_)
    analiz_month = int(actual_datetime.month) - int(month)
    date_ = actual_datetime.strftime("%d")
    day_now = actual_datetime.weekday()
    
    #print(analiz_month)
    if analiz_month == 1 and (int(date_) == 1 or int(date_) == 2 or int(date_) == 3 or int(date_) == 4) and (day_now == 1 or day_now == 2 or day_now == 3 or day_now == 4):
        
        print(analiz_month, int(date_), day_now)
    if (int(date_) == 1 or int(date_) == 2) and day_now == 0:
        print(analiz_month, int(date_), day_now, 'lllllllllll')
        
        
