# DZ11

from collections import UserDict
from datetime import date, datetime
import os
import re


class Field:
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація клас
    pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)
    def validate(self, phone):        
        long_ = len(phone)
        rah = 0
        if long_ == 10:
            return phone
        else:
            rah += 1
            while rah < 100:
                print("Введіть 10-значний номер")
                
                
class Birthday(Field):
    # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)        
            
    def validate(self, birth):        
        long_ = len(phone)
        rah = 0
        if long_ == 10:
            return phone
        else:
            rah += 1
            while rah < 100:
                print("Введіть день народження у такому форматі: спочатку РІК, потім місяць ММ, потім день ДД,\nнаприклад: 2000 12 31")
        
   
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
        day_now = date.today() 
        self.birth_yer = birth_yer
        self.birth_mont = birth_mont
        self.birth_day = birth_day
        birth = date(self.birth_yer, self.birth_mont, self.birth_day)
        Birthday.validate(self, birth)
        dniv = birth - day_now
        if dniv == 0:
            txt_dniv = f'Сьогодні день народження у {Name_}'
        if dniv < 0:    
            txt_dniv = f'У цьому році день народження у {Name_} вже минув'     
        if dniv > 0:
            txt_dniv = f'До дня народження {Name_} залишилося днів - {dniv}'    
        return txt_dniv       
             
        
    def remove_phone(self, phone):
        try:
            self.phone = phone        
            self.phones.remove(self.phone)        
            phones_ = self.phones  
            return phones_
        except ValueError:
            dd = f"Телефон {self.phone} відсутній"     
            print(dd)
            #return phones_
        
    
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
        self.data.update({Name_: phones_})   
        
            
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
        a_ = f'DELETED {rec}'
        print(a_)
        
    
        # Створення нової адресної книги
data = {}
phones = []
phones_ = []
phone = ''

book = AddressBook(data, phones)
                     

    # Створення запису для John
john_record = Record("John")
Name_ = john_record.name.value

john_record.add_phone("1234567890")
phones_ = john_record.add_phone("5555555555")
birth_ = john_record.days_to_birthday(1967, 12, 10)
print(birth_)
#john_record.remove_phone("1234567890")


    # Додавання запису John до адресної книги

book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
Name_ = jane_record.name.value
phones_ = jane_record.add_phone("9876543210")
#phones_ = jane_record.remove_phone("9876543210")
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