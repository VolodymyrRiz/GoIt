# DZ10

from collections import UserDict

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
    pass
   

class Record:
   
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        #Record.name.value
        
    # реалізація класу

        
    def add_phone(self, phone):        
               
        self.phone = phone        
        self.phones.append(self.phone)        
        phones_ = self.phones        
        return phones_
        
        
    def remove_phone(self):
        pass
    
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

    # Додавання запису John до адресної книги

book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
Name_ = jane_record.name.value
phones_ = jane_record.add_phone("9876543210")
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

    # Видалення запису Jane
book.delete("Jane")