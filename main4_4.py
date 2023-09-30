key = None
grade = dict()

def get_grade(key):

    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}  #
    return grade.get(key, None)
    
    
def get_description(key):
    print(type(key))
        
    grade = {              
        'F': 'Unsatisfactorily', 
        'FX': 'Unsatisfactorily', 
        'E': 'Enough', 
        'D': 'Satisfactorily', 
        'C': 'Good', 
        'B': 'Very good', 
        'A': 'Perfectly'}
    
    return grade.get(key, None)
            
        
print(get_grade(key))
#print(get_grade(get_grade(key)))
print(get_description(key))     
