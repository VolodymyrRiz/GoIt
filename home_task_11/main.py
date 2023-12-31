# DZ11

from collections import UserDict
from datetime import date, datetime, timedelta
import os
import re


class Field:
    
    def __init__(self, value):
        self.__value = None
        self.value = value
        
    @property    
    def __str__(self):
        return str(self.__value)
    
    @__str__.setter
    def __str__(self):
        return str(self.__value)
       
class Name(Field):
    # реалізація клас
    pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        #self.__phone = None
        self.phone = value
        self.validate(value)
        super().__init__(value)
            
         
    def validate(self, phone):    
        while True:
            
            self.phone = phone
            long_ = len(self.phone)
            symb = str(self.phone).isnumeric()
            
            if long_ == 10 and symb == True:
                return self.phone
            else:
                print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
                phone = input()
                
                
class Birthday(Field):
#     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.birth = self.value
        return self.birth        
     
        
    def validate(self, txt_valid):   
        self.txt_valid = txt_valid         
        self.txt_valid = "Введіть день народження у такому форматі: спочатку РІК, потім місяць ММ, потім день ДД,\nнаприклад: 2000 12 31"
        return self.txt_valid
   
class Record:
   
    def __init__(self, name):
        self.name = Name(name)        
        self.phones = []
                
    # реалізація класу
        
    def add_phone(self, phone):                
        
        self.phone = phone                 
        Phone.validate(self, self.phone)
        self.phones.append(self.phone)        
        phones_ = self.phones        
        return phones_
    
    def days_to_birthday(self, birth_yer, birth_mont, birth_day):
        txt_valid = ' '
        day_now = date.today() 
        rik = day_now.year
        self.birth_yer = birth_yer
        
        self.birth_mont = birth_mont
        
        self.birth_day = birth_day
        
        try:
            birth = date(rik, self.birth_mont, self.birth_day)        
            dniv = int((birth - day_now).days)
            if dniv == 0:
                print(f'Сьогодні день народження у {Name_}')
            if dniv < 0:    
                print(f'У цьому році день народження у {Name_} вже минув')     
            if dniv > 0:
                print(f'До дня народження {Name_} залишилося днів - {dniv}')   
            birth = date(self.birth_yer, self.birth_mont, self.birth_day)
        except:
            Birthday.validate(self, txt_valid)
            print(self.txt_valid)
            birth = []          
        return birth                  
        
    def remove_phone(self, phone):
        try:
            self.phone = phone        
            self.phones.remove(self.phone)        
            phones_ = self.phones  
            return phones_
        except ValueError:
            dd = f"Телефон {self.phone} відсутній"     
            print(dd)
                    
    
    def edit_phone(self, a, b):
        index_ = self.phones.index(a)
        self.phones[index_] = b        
        pass    
       
    def __str__(self):       
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self, data, phones):
        self.data = data
        self.phones = phones
    
    def add_record(self, *argv, **kwarg):            
        self.data.update({Name_: phones_, Name_+'_birthday': birth_})   
        if flag_new == 1:
            return
                
            
    def find(self, name):
        if name in self.data:
            return name       
        
    def find_phone(self, ph_):
        
        for dict_ in self.data.items():            
            count_ = str(dict_).count(str(ph_))            
            if count_ > 0:                
                return ph_
            if count_ == 0:
                print('Телефон не знайдено')
                return
            else:
                continue
                 
    
    def delete(self, rec):        
        self.data.pop(rec)
        self.data.pop(rec+'_birthday')
        a_ = f'DELETED RECORD {rec}'
        print(a_)
                       
        
    def iterator(self, item_number):
        self.item_number = item_number               
        counter_ = 0
        counterr_ = 0
        resultt = ''
        len_data = len(self.data)
        
        for item_, recordd in self.data.items():            
            resultt += f'{item_}: {recordd} \n'   
            counter_ += 1
            counterr_ += 1
            if  counterr_ == len_data:
                print(resultt)
                return
            if counter_ == self.item_number:                
                print(resultt)         
                counter_ = 0
                resultt = ''
                print('Продовжити перегляд? Натисніть ENTER')
                inp = input()
        
    
        # Створення нової адресної книги
data = {}
phones = []
phones_ = []
phone = ''
birth = []
flag_new = 0

book = AddressBook(data, phones)

    # Створення запису для John
john_record = Record("John")
Name_ = john_record.name.value
john_record.add_phone("1234567890")
phones_ = john_record.add_phone("5555555555")
birth_ = john_record.days_to_birthday(2023, 12, 23)

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
Name_ = jane_record.name.value
phones_ = jane_record.add_phone("9876543210")
birth_ = jane_record.days_to_birthday(1950, 11, 21)
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name, record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john_record.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = book.find_phone('5555555555')
print(f"{john}: {found_phone}")  # Виведення: 5555555555
phones_ = john_record.remove_phone("1112223333")

    # Видалення запису Jane
book.delete("Jane")

    # ПОСТОРІНКОВИЙ ПЕРЕГЛЯД АДРЕСНОЇ КНИГИ
book.iterator(10) 

# ЗАПОВНЕННЯ АДРЕСНОЇ КНИГИ
while True:
    flag_new = 1
    print('Заповнити адресну книгу? - Enter. Вийти? - q + Enter')
    inp = input()
    if inp == 'q':
        os.abort()
    new_name = ''
    new_phone = ''
    birth_yer = 0
    birth_mont = 0
    birth_day = 0
    
    print("Введіть ім'я та натисність Enter: ")
    new_name = input()
    
    new_record = Record(new_name)
    Name_ = new_record.name.value
        
    print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
    new_phone = input()

    phones_ = new_record.add_phone(new_phone)
    
    print("Введіть дату народження.")
    print("Рік? (чотири цифри + Enter): ")
    birth_yer = int(input())
   
    print("Місяць? (дві цифри + Enter): ")
    birth_mont = int(input())
    
    print("День? (дві цифри + Enter): ")
    birth_day = int(input())
    

    birth_ = new_record.days_to_birthday(birth_yer, birth_mont, birth_day)
    book.add_record(new_record)