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
        
    date_now = datetime(year=2023, month=10, day=23)   
    #date_now = date.today()
    
    day_now = date_now.weekday()
    
    day_now_word = date_now.strftime("%A")
    month = date_now.strftime("%m")
    date_ = date_now.strftime("%d")
        
    if day_now == 5 or day_now == 6:
        a = '''Дні народження в суботу та неділю цього тижня 
будуть включені в понеділок наступного тижня,
якщо ви сформуєте розклад на наступний тиждень 
з понеділка'''
        print(a)
        return user_week
        
    for day in range(day_now, 5):        
        key_dict = []               
        day_next = day
        
        
     # Обробка вихідних днів   
        if day == 0:
                          
            for dict in users:                   
                
                for key, value in dict.items():
                    pass
                   
                value_month = value.strftime('%m')
                
                value_date_next = value.strftime('%d')
                if int(value_date_next) == int(date_) - 2:
                   
                    day_next_word = 'Monday'
                if int(value_date_next) == int(date_) - 1:
                  
                    day_next_word = 'Monday'
                
                if value_month == month and int(value_date_next) == int(date_) - 2: 
                           
                    value = dict.get('name')
                    key_dict.append(value)  
                    
                    user_week.update({day_next_word: key_dict}) 
                   
                if value_month == month and int(value_date_next) == int(date_) - 1: 
                            
                    value = dict.get('name')
                    key_dict.append(value)  
                       
                    user_week.update({day_next_word: key_dict}) 
            
     # Обробка актуального дня               
        if day == day_now:
            
            for dict in users:
                                
                for key, value in dict.items():
                    pass
                   
                value_month = value.strftime('%m')
                value_date = value.strftime('%d')
                                
                if value_month == month and value_date == date_:
                    
                    value = dict.get('name')
                    key_dict.append(value)    
                    user_week.update({day_now_word: key_dict})                          
                       
        
     # Обробка наступних днів   
        
        
        if day_next == 1:
            day_next_word = 'Tuesday'    
            for dict in users:
                    
                
                for key, value in dict.items():
                    pass
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                            
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 1:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                              
        if day_next == 2:
            day_next_word = 'Wednesday'         
            for dict in users:                     
                
                for key, value in dict.items():
                    pass
               
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 2:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                                
        if day_next == 3:
            day_next_word = 'Thursday'    
            for dict in users:
                                
                for key, value in dict.items():
                    pass
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 3:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict})                     
        
        if day_next == 4:
            day_next_word = 'Friday'          
            for dict in users:                     
                
                for key, value in dict.items():
                    pass
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
               
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 4:
                                
                    print(day_next_word)
                    print(key_dict)
                    value = dict.get('name')
                    print(value)
                    key_dict.append(value)   
                    print(key_dict)
                    user_week.update({day_next_word: key_dict}) 
                   
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
