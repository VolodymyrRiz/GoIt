key = dict()


def get_grade(key):
    
   

    key = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}

    for key_select in key.values():
         if key_select == None:
             return
         print(key_select)
    return
    
    


def get_description(key):
    key = {
        'F': 'Unsatisfactorily', 
        'FX': 'Unsatisfactorily', 
        'E': 'Enough', 
        'D': 'Satisfactorily', 
        'C': 'Good', 
        'B': 'Very good', 
        'A': 'Perfectly'}
    
    for key_select in key.values():
         if key_select == None:
             return
         print(key_select)
    return
    
        
        
get_grade(key) 
get_description(key)    
