from datetime import date, datetime
user_week = {'Monday': [], 
             'Tuesday': [], 
             'Wednesday': [], 
             'Thursday': [], 
             'Friday': [], 
             'Saturday': [],
             'Sunday': [],
             }

users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Grot", "birthday": datetime(1957, 2, 1).date()},
        {"name": "Jan Swift", "birthday": datetime(1977, 12, 5).date()},
        {"name": "Jan Forest", "birthday": datetime(1978, 12, 5).date()},
        {"name": "Jan Tard", "birthday": datetime(1980, 11, 3).date()},
        {"name": "Jan Weis", "birthday": datetime(1990, 11, 4).date()},
        {"name": "Jan Flint", "birthday": datetime(1972, 10, 25).date()},
        {"name": "Jan Boss", "birthday": datetime(1976, 10, 30).date()},
        {"name": "Jan Grape", "birthday": datetime(1977, 11, 1).date()},
        {"name": "Jan Bad", "birthday": datetime(1977, 11, 5).date()},
    ]

key_dict = []

date_now = datetime.now().date()
#print(date_now)
day_now = date_now.weekday()
month = date_now.strftime("%m")
date = date_now.strftime("%d")
#print(month)

for day in range(day_now, 7):
    #print(day)
    if day == 0:
        name = users.get('name')
        #print(name)
    elif day == 2:
        for dict in users:
            #print(dict)
            
            for key, value in dict.items():
                pass
                #print(type(value))
            value_month = value.strftime('%m')
            value_date = value.strftime('%d')
            #print(value_day)
            print(str(day_now))
            
            if value_month == month and value_date == date:
                #print("kkkkkkkkkkkkkkkkkkk")
                value = dict.get('name')
                key_dict.append(value)             
                print(key_dict)
            
                
            
                