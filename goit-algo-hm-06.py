from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        self.validate_phone(value)
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
             if not re.fullmatch(r'\d{10}', value):
                  raise ValueError('Phone number must be 10 digits')
             

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
          if not isinstance(phone,Phone):
               raise ValueError("Please correct the phone number")
          self.phones.append(phone)

    def remove_phone(self, phone):
        if not isinstance(phone, Phone):
             raise ValueError("Please correct the phone number")
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        try:
            Phone(new_phone)
        except ValueError as e:
            return str(e)
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f'Phone number has changed from {old_phone} to {new_phone} for {self.name.value}'
        return f'Phone number {old_phone} not found for {self.name.value}'
                 
    def find_phone(self, phone: Phone):
        matching_phones = list(filter(lambda p: p.value == phone.value, self.phones ))
        return matching_phones[0] if matching_phones else None

class AddressBook(UserDict):
    
     def add_record(self, record):
           if not isinstance(record, Record):
                raise ValueError()
           self.data[record.name] = record
     
     def find(self, name: str) -> Record:
            return self.data.get(name)
     
     def delete(self, name:str):
              if name in self.data:
                   del self.data[name]

