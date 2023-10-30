# ДЗ9
# "hello", відповідає у консоль "How can I help you?"

import os
calc = 0

def hello(txt):
    return txt

def add(txt):
    return txt


def main(prin_inp):
    global calc
    calc += 1   
    print(calc)
    print(a)
    if calc == 10:
        print("Don't make fun of me, 5 more mistakes and I'm done")
    if calc == 15:
        print('Good bye!!!')        
        return os.abort()
    
    d = input()
    
    if d == 'hello' or d == 'Hello' or d == 'HELLO':
           
        print('How can I help you?')
        d = input()
        
        
    elif d == '.':
        print('Good bye. See you later!')        
        return os.abort()
    else:
        print("You didn't say hello. Try again...")
        return
           

a = '''
My name is SYSTEM BOT. 
I can help you to work with contacts and their phone numbers.
Are you ready to communicate? 
If you are ready tell me HELLO (print please)
or print . for exit
'''
while True:
    main(a)

