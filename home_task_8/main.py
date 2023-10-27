from datetime import date, datetime

user_week = {'Monday': [], 
             'Tuesday': [], 
             'Wednesday': [], 
             'Thursday': [], 
             'Friday': [], 
            #  'Saturday': [],
            #  'Sunday': [],
             }


def get_birthdays_per_week(users):
    
    key_dict = []
    #count_day = 1
    #value_true = None
    
    date_now = datetime(year=2023, month=10, day=23)
    #date_now = datetime.now().date()
    #date_now = date.today()
    #print(date_now)
    day_now = date_now.weekday()
    #print(day_now)
    day_now_word = date_now.strftime("%A")
    month = date_now.strftime("%m")
    date_ = date_now.strftime("%d")
    #print(date_)
    
    if day_now == 5 or day_now == 6:
        a = '''Дні народження в суботу та неділю цього тижня 
будуть включені в понеділок наступного тижня,
якщо ви сформуєте розклад на наступний тиждень 
у понеділок'''
        print(a)
        return user_week
        
    for day in range(day_now, 5):
        #print(day)
        key_dict = []       
        #end_of_week = 7 - day_now #7
        #end_date_week = int(date_) + end_of_week - 2 #21
        #print(end_date_week)
        day_next = day
        
        #print(day_next)
        
        if day == 0:
            #end_of_week = 7 - day_now #4
            #end_date_week = int(date) + end_of_week - 2 #27
            #print(end_date_week)
            
            #print(day_next)
               
            for dict in users:
                #print(dict)        
                
                for key, value in dict.items():
                    pass
                    #print(type(value))
                value_month = value.strftime('%m')
                #print('   ', value_month)
                value_date_next = value.strftime('%d')
                if int(value_date_next) == int(date_) - 2:
                    #day_next = 5
                    day_next_word = 'Monday'
                if int(value_date_next) == int(date_) - 1:
                    #day_next = 6
                    day_next_word = 'Monday'
                #print(value_date_next)
                            
                #print(day_next_word)
                #print(value_day)
                #print(str(day_now))
                #print(type(value)) 
                #print(';;;;;;', day_next)
                if value_month == month and int(value_date_next) == int(date_) - 2: 
                     #and day_next == 5        
                    value = dict.get('name')
                    key_dict.append(value)  
                    #print('iiiiiiiiiiiiiiiiiiiiiiii')
                    #print(key_dict)  
                    user_week.update({day_next_word: key_dict}) 
                    #count_day += 1     
                    #day_next = 6 
                    #value_true = value
                if value_month == month and int(value_date_next) == int(date_) - 1: 
                     #and day_next == 6            
                    value = dict.get('name')
                    key_dict.append(value)  
                    #print(key_dict)    
                    user_week.update({day_next_word: key_dict}) 
            #print(user_week)  
                    
        if day == day_now:
            #print(day_now)
            for dict in users:
                #print(dict)
                
                for key, value in dict.items():
                    pass
                    #print(type(value))
                value_month = value.strftime('%m')
                value_date = value.strftime('%d')
                #print(value_date)
                #print(str(day_now))
                
                if value_month == month and value_date == date_:
                    #print("kkkkkkkkkkkkkkkkkkk")
                    value = dict.get('name')
                    key_dict.append(value)    
                    user_week.update({day_now_word: key_dict})  
                        
                #print(user_week)           
        
        
        
        #day_next = day_now + count_day    #1
        if day_next == 1:
            day_next_word = 'Tuesday'    
            for dict in users:
                #print(dict)        
                
                for key, value in dict.items():
                    pass
                    #print()
                value_month = value.strftime('%m')
                #print(value_month)
                value_date_next = value.strftime('%d')
                #print(value_date_next)
            
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 1:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                    #count_day += 1     
            #day_next = day_now + count_day
            #print(day_next)
            #key_dict = []     
            
        if day_next == 2:
            day_next_word = 'Wednesday'         
            for dict in users:
                #print(dict)        
                
                for key, value in dict.items():
                    pass
                    #print()
                value_month = value.strftime('%m')
                #print(value_month)
                value_date_next = value.strftime('%d')
                #print(value_date_next)
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 2:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                    #count_day += 1     
            #day_next = day_now + count_day
            #key_dict = []  
            
        if day_next == 3:
            day_next_word = 'Thursday'    
            for dict in users:
                #print(dict)        
                
                for key, value in dict.items():
                    pass
                    #print()
                value_month = value.strftime('%m')
                #print(value_month)
                value_date_next = value.strftime('%d')
                #print(value_date_next)
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 3:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                    #count_day += 1     
            #day_next = day_now + count_day 
            #key_dict = []       
        
        if day_next == 4:
            day_next_word = 'Friday'          
            for dict in users:
                #print(dict)        
                
                for key, value in dict.items():
                    pass
                    #print()
                value_month = value.strftime('%m')
                #print(value_month)
                value_date_next = value.strftime('%d')
                #print(value_date_next)
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 4:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                #key_dict = []  
                    #count_day += 1           
                  
                    #value_true = value
            #print(user_week)
    
    users = user_week
            

    # Реалізуйте тут домашнє завдання
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 1).date()},
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

    result = get_birthdays_per_week(users)
    #print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
