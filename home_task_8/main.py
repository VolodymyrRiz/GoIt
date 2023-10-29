from datetime import date, datetime

user_week = {'Monday': [], 
             'Tuesday': [], 
             'Wednesday': [], 
             'Thursday': [], 
             'Friday': [], 
            }


def get_birthdays_per_week(users):
    
    b = "Робити календар днів народжень із сьогоднішнього дня\n чи з наступного понеділка або якогось наступного дня?\n З наступного понеділка або якогось наступного дня? Натиснйть 1.\n З сьогоднішнього дня? Натисніть 0." 
    print(b)   
    d = input()
    
    if d == '1':
        print('Уведіть число дня')
        d = int(input())
        date_now = date.today() 
        rik = date_now.year
        misiac = date_now.month
        den = date_now.day     
        
        date_now = datetime(rik, misiac, d) 
        
    else:
        date_now = date.today()        
          
    key_dict = []             
     
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
        
    for day_ in range(day_now, 5):        
        key_dict = []               
        day_next = day_
        
        
     # Обробка вихідних днів   
        if day_ == 0:
                          
            for dict in users:                   
                
                for key, value in dict.items():
                    pass
                
                
                same_day = value.day
                same_month = value.month                
                now_year = date_now.year      
                try:
                    
                    actual_datetime = datetime(now_year, same_month, same_day).date()                      
                except ValueError:
                    actual_datetime = datetime(now_year, same_month, same_day - 1).date()    
                                 
                value = actual_datetime
                value_month = value.strftime('%m')                               
                value_date_next = value.strftime('%d')
                value_date_next = int(value_date_next)                
                day_prev = value.weekday()                        
                   
                
                if (value_date_next == 31 or value_date_next == 30) and value_month != 2 and value_month != 12 and same_day == 1 and (day_prev == 5 or day_prev == 6):
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict}) 
                                     
                    
                if int(value_date_next) == 29 and int(value_month) == int(month) - 1 and int(value_month) != 2 and int(value_month) != 12 and day_prev == 5 and same_day == 1:
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})   
                   
                    
                if (int(value_date_next) == 28 or int(value_date_next) == 29) and int(value_month) == 2 and int(value_month) != 12 and (day_prev == 5 or day_prev == 6) and same_day == 1:
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})   
                    
                    
                if int(value_date_next) == 27 and int(value_month) == 2 and int(value_month) != 12 and int(value_month) == int(month) - 1 and day_prev == 5 and same_day == 1:
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})   
                    
                    
                if (int(value_date_next) == 31 or int(value_date_next) == 30) and int(value_month) != 2 and int(value_month) == 12 and int(month) == 1:
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})    
                                       
                                
                if value_month == month and int(value_date_next) == int(date_) - 2:                            
                    day_next_word = 'Monday'
                    value = dict.get('name')
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict}) 

                   
                if value_month == month and int(value_date_next) == int(date_) - 1:  
                    day_next_word = 'Monday'                           
                    value = dict.get('name')
                    key_dict.append(value)                         
                    user_week.update({day_next_word: key_dict})                                
            
     # Обробка актуального дня               
        if day_ == day_now:
            
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
                
                same_day = value.day
                same_month = value.month                
                now_year = date_now.year               
                try:
                    
                    actual_datetime = datetime(now_year, same_month, same_day).date()                      
                except ValueError:
                    actual_datetime = datetime(now_year, same_month, same_day - 1).date()    
                value = actual_datetime
             
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                analiz_month = int(actual_datetime.month) - int(month)
                date_ = actual_datetime.strftime("%d")
                day_now = actual_datetime.weekday()
                
                if analiz_month == 1 and (int(date_) == 1 or int(date_) == 2 or int(date_) == 3 or int(date_) == 4) and day_now == 1:
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})    
                         
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 1:
                                
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict}) 
                              
        if day_next == 2:
            day_next_word = 'Wednesday'         
            for dict in users:                     
                
                for key, value in dict.items():
                    pass
               
                same_day = value.day
                same_month = value.month                
                now_year = date_now.year               
                try:
                    
                    actual_datetime = datetime(now_year, same_month, same_day).date()                      
                except ValueError:
                    actual_datetime = datetime(now_year, same_month, same_day - 1).date()    
                value = actual_datetime             
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                analiz_month = int(actual_datetime.month) - int(month)
                date_ = actual_datetime.strftime("%d")
                day_now = actual_datetime.weekday()
                
                if analiz_month == 1 and (int(date_) == 1 or int(date_) == 2 or int(date_) == 3 or int(date_) == 4) and day_now == 2:
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})                  
                               
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 2:
                                
                    value = dict.get('name')                    
                    key_dict.append(value)                     
                    user_week.update({day_next_word: key_dict}) 
                                
        if day_next == 3:
            day_next_word = 'Thursday'    
            for dict in users:
                                
                for key, value in dict.items():
                    pass
                    
                same_day = value.day
                same_month = value.month                
                now_year = date_now.year               
                try:
                    
                    actual_datetime = datetime(now_year, same_month, same_day).date()                      
                except ValueError:
                    actual_datetime = datetime(now_year, same_month, same_day - 1).date()    
                value = actual_datetime
             
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                analiz_month = int(actual_datetime.month) - int(month)
                date_ = actual_datetime.strftime("%d")
                day_now = actual_datetime.weekday()
                
                if analiz_month == 1 and (int(date_) == 1 or int(date_) == 2 or int(date_) == 3 or int(date_) == 4) and day_now == 3:
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})   
                
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 3:
                                
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})                     
        
        if day_next == 4:
            day_next_word = 'Friday'          
            for dict in users:                     
                
                for key, value in dict.items():
                    pass
                    
                same_day = value.day
                same_month = value.month                
                now_year = date_now.year               
                try:
                    
                    actual_datetime = datetime(now_year, same_month, same_day).date()                      
                except ValueError:
                    actual_datetime = datetime(now_year, same_month, same_day - 1).date()    
                value = actual_datetime
             
                    
                value_month = value.strftime('%m')                
                value_date_next = value.strftime('%d')
                
                analiz_month = int(actual_datetime.month) - int(month)
                date_ = actual_datetime.strftime("%d")
                day_now = actual_datetime.weekday()
                
                if analiz_month == 1 and (int(date_) == 1 or int(date_) == 2 or int(date_) == 3 or int(date_) == 4) and day_now == 4:
                    value = dict.get('name')                    
                    key_dict.append(value)                      
                    user_week.update({day_next_word: key_dict})   
               
                if value_month == month and day_next > day_now and int(value_date_next) == int(date_) + 4:
                                
                    value = dict.get('name')                    
                    key_dict.append(value)                       
                    user_week.update({day_next_word: key_dict}) 
                   
    users = user_week
            

    # Реалізуйте тут домашнє завдання
    return users


if __name__ == "__main__":
    
    users = [{"name": "Jan Koum", "birthday": datetime(2020, 2, 29).date()},
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
    #print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
