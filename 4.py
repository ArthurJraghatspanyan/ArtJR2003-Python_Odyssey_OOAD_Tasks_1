# Modify the Person class to make the age attribute private. Provide a method to get the age (get_age) and another method to set the age (set_age) with

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
    def setAge(self, value):
        if value <= 0:
            raise ValueError("Value can't be less than 0 or equal to it")
        self.__age = value

    def displayPerson(self):
        print(f"This is {self.name} and he is {self.__age} years old")

    def greet(self):
        print(f"Hello, {self.name} and welcome!")

ob = Person("John", 25)
ob.displayPerson()
ob.setAge(22)
ob.displayPerson()
ob.setAge(-22) # ValueError
ob.displayPerson()