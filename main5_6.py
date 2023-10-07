spam_words = ['']
text = ''
argv = ''
new_spam_1 = ''   
new_spam_2 = ''   
new_spam_3 = ''   
   
i = 0

def space_around_def(*argv):
    global spam
    global new_spam_1 
    global new_spam_2 
    global new_spam_3 
    
    if spam.istitle() == True:        
        new_spam_1 = f'{spam} '.lower() 
    else:
        new_spam_1 = f'---'
    new_spam_2 = f' {spam}'.lower()   
    new_spam_3 = f' {spam} '.lower()
    #space_around = True
    
    return new_spam_1, new_spam_2, new_spam_3

    
def is_spam_words(text, spam_words, space_around=False):
    
    global spam
    global new_spam_1 
    global new_spam_2 
    global new_spam_3
    
    for spam in spam_words:  
        while space_around == False:  
            i = text.find(spam)
            if i > -1:                
                return True
            else:
                return False     
        space_around = True        
        while space_around:            
            space_around_def(spam)
            
            text = text.lower()
            i = text.find(new_spam_1)
            if i > -1:                
                return True
           
            i = text.find(new_spam_2)
            if i > -1:               
                return True
            
            i = text.find(new_spam_3)
            if i > -1:
                return True
            
            return False

                              
print(is_spam_words(text, spam_words, space_around=False))
                        
            