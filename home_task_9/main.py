# ДЗ9
# "hello", відповідає у консоль "How can I help you?"

import os
import re

calc = 0

def parser_commands(d, commands):
    
    num = 0
    for com in commands:
        num = d.count(' ')
        if com in d and num == 2 and ('add' in d or 'add' in d or 'Add' in d or 'ADD' in d):            
            b = "I'm doing... Whait please!"
            d = com                     
            return d, b
        elif com in d and num == 2 and ('change' in d or 'change' in d or 'Change' in d or 'CHANGE' in d):            
            b = "I'm doing... Whait please!"
            d = com                     
            return d, b
        elif com in d and (num < 2 or num > 2) and (not 'Show' in d or not 'Show' in d or not 'show' in d or not 'SHOW' in d) and (not 'Phone' in d or not 'Phone' in d or not 'phone' in d or not 'PHONE' in d):           
            b = '...enter only three words: add name phone_number...'
            d = num
            return d, b
        elif com in d and 'Show' in d or 'Show' in d or "SHOW" in d or 'show' in d:
            b = 'Please, there are all your contacts: '            
            return d, b
        elif com in d and 'Phone' in d or 'Phone' in d or "PHONE" in d or 'phone' in d:
            num = d.count(' ')
            if num == 1:
                imia = d[6:].strip()
                d = imia
                b = "I'm looking for a phone..."
            else:
                b = '''I advise you to first view the names in the contacts with the show all command 
            so as not to make a mistake in writing the name, 
            and then enter the phone command and the correct name after a space'''       
            return d, b
        elif com in d and 'good bye' in d or 'good bye' in d or "Good bye" in d or 'GOOD BYE' in d or 'close' in d or "Close" in d or 'CLOSE' in d or 'exit' in d or "Exit" in d or 'EXIT' in d or 'quit' in d or "Quit" in d or 'QUIT' in d:
            b = 'Goog bye. I am always happy to help!'
            return d, b
        else:
            continue
        
    flag = 10
    f = input_error(flag)            
    return d, f
    
def input_error(flag):
    #num = int(num)
    try:
        if flag == 10:
            c = 'You can use only such commands:\n"good bye", "close", "exit", "quit", "add...", "change...", "show all", "phone..."'
            return c
        if flag == 9:
            c = 'First you need to enter the command, and then your name and phone number'
            flag = c
            return flag        
        _phone_ = int(flag)
        if type(_phone_) is int:
            flag = _phone_
            return flag
    except ValueError:
        c = 'The third word in the add command must be a numeric phone number'            
        flag = c
        return flag  
        

def handler_change(add_):
    com_, name_, phone_ = add_.split(' ')
    
    if com_ != 'change' and com_ != 'CHANGE' and com_ != 'Change':
        flag = 9
        add_= input_error(flag)        
        return add_
    elif com_ == 'change' or com_ == 'Change' or com_ == 'CHANGE':
        flag = phone_        
        add_ = input_error(flag)
        if not type(add_) is int:   
            return add_
        else:        
           
            file_ = open('phone_dict.txt')            
            phone_dict = file_.read()
            file_.close()            
            phone_dict = phone_dict[1:-1]
            phone_dict = phone_dict.replace(':', ',')
            phone_dict_list = phone_dict.split(',')
            cnt_ = 0
            len_ = 0
            phone_dict = {}
            while len_ != len(phone_dict_list):
                if cnt_ == 0:
                    word1 = phone_dict_list[0].strip()
                    word1 = word1[1:-1]
                    phone_dict_list.pop(0)
                    cnt_ += 1
                if cnt_ == 1:
                    word2 = phone_dict_list[0].strip()
                    word2 = int(word2)
                    phone_dict_list.pop(0)
                    cnt_ = 0
                phone_dict.update({word1: word2})
            phone_dict.update({name_: add_}) # add_ номер телефону як int
            
            file_ = open('phone_dict.txt', 'w')
            file_.write(str(phone_dict))
            file_.close() 
            
            add_ = f'The name {name_} and phone number {add_} are recorded'
            return add_
    
def handler_phone(add_):
    file_ = open('phone_dict.txt')            
    phone_dict = file_.read()
    file_.close() 
    imia_pos = phone_dict.find(add_)
    if add_ in phone_dict:
        phone_dict_part = phone_dict[imia_pos:]
        imia_nomer = re.search('\d+', phone_dict_part)
        add_ = imia_nomer.group()
    
        return add_
    else:
        add_ = "Name not found!"

def handler_show_all(add_):    
    
    file_ = open('phone_dict.txt')            
    phone_dict = file_.read()
    file_.close() 
    add_ = phone_dict    
    return add_

def handler_exit(add_):
    return os.abort()

def handler_add(add_):
    com_, name_, phone_ = add_.split(' ')
    
    if com_ != 'add' and com_ != 'ADD' and com_ != 'Add':
        flag = 9
        add_= input_error(flag)        
        return add_
    elif com_ == 'add' or com_ == 'ADD' or com_ == 'Add':
        flag = phone_        
        add_ = input_error(flag)
        if not type(add_) is int:   
            return add_
        else:        
           
            file_ = open('phone_dict.txt')            
            phone_dict = file_.read()
            file_.close()            
            phone_dict = phone_dict[1:-1]
            phone_dict = phone_dict.replace(':', ',')
            phone_dict_list = phone_dict.split(',')
            cnt_ = 0
            len_ = 0
            phone_dict = {}
            while len_ != len(phone_dict_list):
                if cnt_ == 0:
                    word1 = phone_dict_list[0].strip()
                    word1 = word1[1:-1]
                    phone_dict_list.pop(0)
                    cnt_ += 1
                if cnt_ == 1:
                    word2 = phone_dict_list[0].strip()
                    word2 = int(word2)
                    phone_dict_list.pop(0)
                    cnt_ = 0
                phone_dict.update({word1: word2})
            phone_dict.update({name_: add_}) # add_ номер телефону як int
            
            file_ = open('phone_dict.txt', 'w')
            file_.write(str(phone_dict))
            file_.close() 
            
            add_ = f'The name {name_} and phone number {add_} are recorded'
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
            
            d_, commands_ = parser_commands(d, commands)
            print(commands_)
            if d_ == 'add' or d_ == 'Add' or d_ == 'ADD':                
                print(handler_add(add_))
            if d_ == 'change' in d or 'Change' in d or 'CHANGE' in d:
                print(handler_change(add_))
            if 'phone' in add_ or 'Phone' in add_ or "PHONE" in add_:
                add_ = d_
                print(handler_phone(add_))
            if d_ == 'show all' or d_ == 'Show all' or d_ == 'SHOW ALL':
                print(handler_show_all(add_))
            if d_ == 'good bye' in d or 'Good bye' in d or 'GOOD BYE' in d or 'close' in d or 'Close' in d or 'CLOSE' in d or 'exit' in d or 'Exit' in d or "EXIT" in d or 'quit' in d or "Quit" in d or 'QUIT' in d:
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

commands = [
            "good bye", 
            "close", 
            "exit", 
            "quit", 
            "add", 
            "change", 
            "show all", 
            "phone",
            "Good bye", 
            "Close", 
            "Exit", 
            "Quit", 
            "Add", 
            "Change", 
            "Show all", 
            "Phone",
            "GOOD BYE", 
            "CLOSE", 
            "EXIT", 
            "QUIT", 
            "ADD", 
            "CHANGE", 
            "SHOW ALL", 
            "PHONE",
            ]

phone_dict = {}

while True:
    main(a, commands)

