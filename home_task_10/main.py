# DZ10

from collections import UserDict


class Field:
    
    def __init__(self, value):
        self.value = value   
        #print(self.value)     

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return str(self.name)       
       
    
class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
        
    def __str__(self):
        return str(self.phone)   
    # реалізація класу     


class Record:
   
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        #Record.name.value
        
    # реалізація класу

        
    def add_phone(self, phone):
    
        self.phone = phone
        return self.phone
        
    def remove_phone(self):
        pass
    
    def edit_phone(self, *argv, **kwarg):
        pass
    
    def find_phone(self, phone):
        self.phone = phone
        count_phone = self.phones.count(self.phone)
        if count_phone > 0:              
            return print(self.phone)
        else:
            print('jkjkjkjljljljlkjlk')
    
    def __str__(self):
        #print(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}")
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    
    #book_phone = {Record.name.value: Record}
    # реалізація класу
#     Реалізовано метод add_record, який додає запис до self.data.
# Реалізовано метод find, який знаходить запис за ім'ям.
# Реалізовано метод delete, який видаляє запис за ім'ям.
# Записи Record у AddressBook зберігаються як значення у с.vловнику. В якості ключів використовується значення Record.name.value.
    def add_record(self, *argv):    
        record = book.data.update({Name: Phone})
        print(book.data)
        
        return record
        
            
    def find(self, name):
        if name in book.data:
            print(name)   
        else:
            print('jjjjjjjjjjj')   
            pass      
    
    def delete(self, name):
        book.delete("Jane")
        print(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)} is deleted")

    
        # Створення нової адресної книги
book = AddressBook()

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
    print(book.data)
    print('nnnnnnnnnn', record)
    pass

    # Знаходження та редагування телефону для John
john = book.find("John")
john_record.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
