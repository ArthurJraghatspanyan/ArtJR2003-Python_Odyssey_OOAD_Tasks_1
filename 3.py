# Add a method to the Person class called greet that prints a greeting message including the person’s name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print(f"This is {self.name} and he is {self.age} years old")

    def greet(self):
        print(f"Hello, {self.name} and welcome!")

ob = Person("John", 25)
# ob.displayPerson()
ob.greet()