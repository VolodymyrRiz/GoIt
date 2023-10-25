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
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}, #четвер
        {"name": "Jan Grot", "birthday": datetime(1957, 2, 1).date()},#пятниця
        {"name": "Jan Swift", "birthday": datetime(1977, 12, 5).date()},#неділя
        {"name": "Jan Forest", "birthday": datetime(1978, 12, 5).date()},#
        {"name": "Jan Tard", "birthday": datetime(1980, 11, 3).date()},#
        {"name": "Jan Weis", "birthday": datetime(1990, 11, 4).date()},#
        {"name": "Jan Flint", "birthday": datetime(1972, 10, 31).date()},#
        {"name": "Jan Boss", "birthday": datetime(1976, 10, 27).date()},#
        {"name": "Jan Grape", "birthday": datetime(1977, 11, 1).date()},#
        {"name": "Jan Bad", "birthday": datetime(1977, 11, 5).date()},#
    ]

key_dict = []
count_day = 1
value_true = None


date_now = datetime.now().date()
#print(date_now)
day_now = date_now.weekday()
day_now_word = date_now.strftime("%A")
month = date_now.strftime("%m")
date = date_now.strftime("%d")
#print(month)

for day in range(day_now, 7):
    #print(day)
    if day == 0:
        name = users.get('name')
        #print(name)
    elif day == day_now:
        for dict in users:
            #print(dict)
            
            for key, value in dict.items():
                pass
                #print(type(value))
            value_month = value.strftime('%m')
            value_date = value.strftime('%d')
            #print(value_date)
            #print(str(day_now))
            
            if value_month == month and value_date == date:
                #print("kkkkkkkkkkkkkkkkkkk")
                value = dict.get('name')
                key_dict.append(value)    
                user_week.update({day_now_word: key_dict})  
                      
                #print(user_week)
                
    
              
    end_of_week = 7 - day_now #4
    end_date_week = int(date) + end_of_week - 2 #27
    #print(end_date_week)
    day_next = day_now + count_day    #4
    
    for dict in users:
        #print(dict)        
          
        for key, value in dict.items():
            pass
            #print(type(value))
        value_month = value.strftime('%m')
        print(value_month)
        value_date_next = value.strftime('%d')
        print(value_date_next)
        day_next_word = value.strftime('%A')
        print(day_next_word)
        #print(value_day)
        #print(str(day_now))
        #print(type(value))  
        if value_month == month and day_next > day_now and day_next <= end_of_week and int(value_date_next) > int(date) and int(value_date_next) <= end_date_week and value_true == None:
                        
            value = dict.get('name')
            key_dict.append(value)    
            user_week.update({day_next_word: key_dict}) 
            count_day += 1     
            day_next = day_now + count_day   
            value_true = value
print(user_week)
            
                
            
                