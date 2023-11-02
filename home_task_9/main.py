# ДЗ9
# "hello", відповідає у консоль "How can I help you?"

import os
calc = 0

def parser_commands(d, commands):
    
    num = 0
    for com in commands:
        num = d.count(' ')
        if com in d and num == 2:            
            b = "I'm doing... Whait please!"
            d = com                     
            return d, b
        elif com in d and (num < 2 or num > 2):
            flag = num
            b = input_error(flag)
            return b
        else:
            continue
        
    flag = 10
    f = input_error(flag)            
    return f
    
def input_error(flag):
    #num = int(num)
    try:
        if flag == 10:
            c = 'You can use only such commands:\n"good bye", "close", "exit", "quit", "add...", "change...", "show all", "phone..."'
            return c
        if flag != 10 and (flag < 2 or flag > 2):
            c = '...enter only three words: add name phone_number...'
            return c
    except:
        pass
        return

def handler_change(txt):
    return txt

def handler_phone(txt):
    return txt

def handler_show_all(txt):    
    return txt

def handler_exit(txt):
    return txt

def handler_add(add_):
    (com_, name_, phone_) = add_.split(' ')
    

    return add_


def main(a, commands):
    global calc
    b = ''
    calc += 1   
    print(a)
    if calc == 10:
        print("Don't make fun of me, 5 more mistakes and I'm done")
    if calc == 15:
        print('Good bye!!!')        
        return os.abort()
    
    d = input()
    
    if d == 'hello' or d == 'Hello' or d == 'HELLO':
        
        while True:
            com_prnt = '''You can use such commands:
        "good bye", "close", "exit", "quit", 
        "add... [instead of ... print name and phone number: add Nick 0000000000]", 
        "change... [replace phone number, print name and new number: change Nick 1111111111]", 
        "phone... [With this command, I display the phone number for the specified contact 
        in the console. Instead of ... enter the name of the contact whose number should be displayed]"
        "show all [display all saved contacts with phone numbers in the console]" 
            
            '''
            print('How can I help you?')
            print(com_prnt)
            d = input()
            add_ = d
            print(parser_commands(d, commands))
            if d == 'add':
                print(handler_add(add_))
            if d == 'change':
                print(handler_change(add_))
            if d == 'phone':
                print(handler_phone(add_))
            if d == 'show all':
                print(handler_show_all(add_))
            if d == 'good bye' or d == 'close' or d == 'exit' or d == 'quit':
                print(handler_exit(add_))
            
        
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

commands = ["good bye", "close", "exit", "quit", "add", "change", "show all", "phone"]

phone_dict = {}

while True:
    main(a, commands)

