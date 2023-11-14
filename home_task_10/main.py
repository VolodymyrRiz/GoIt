# DZ10

from collections import UserDict

class Field:
    
    def __init__(self, value):
        self.value = value
        #print(self.value)

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація клас
    name = ''
    pass

class Phone(Field):
    # реалізація класу
    phone = ''
    pass
   

class Record:
   
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        #Record.name.value
        
    # реалізація класу

        
    def add_phone(self, phone):
        self.phones = []
        print(self.phones)
        print(phone)
        self.phone = phone
        print(self.phone)
    
        #self.phones = phone
        self_phones = self.phones.append(self.phone)
        
        print(self_phones)
        
    def remove_phone(self):
        pass
    
    def edit_phone(self, *argv, **kwarg):
        
        pass
    
    def find_phone(self):
        pass
    
    def __str__(self):
        #print(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}")
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self, data):
        self.data = data
    
    #book_phone = {Record.name.value: Record}
    # реалізація класу
#     Реалізовано метод add_record, який додає запис до self.data.
# Реалізовано метод find, який знаходить запис за ім'ям.
# Реалізовано метод delete, який видаляє запис за ім'ям.
# Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
    def add_record(self, *argv):    
        self.data.update({Name: Phone})   
        print(self.data) 
            
    def find(self, name):
        if name in self.data:
            return name            
    
    def delete(self, data):
        self.data.delete("Jane")
        print(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)} is deleted")

    
        # Створення нової адресної книги
data = {}
book = AddressBook(data)

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


    # Додавання запису John до адресної книги

book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john_record.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")