# Extend the Person class by adding an __init__ constructor method that initializes name and age when an object is created. Ensure the method uses self to assign the values.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print(f"This is {self.name} and he is {self.age} years old")

ob = Person("John", 25)
ob.displayPerson()