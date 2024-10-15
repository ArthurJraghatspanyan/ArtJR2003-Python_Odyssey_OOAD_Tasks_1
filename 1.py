# Write a Python class named Person that has attributes for name and age. Include a method to display the person’s details.

class Person:
    name = "John"
    age = 25
    def displayPerson(self):
        print(f"This is {self.name} and he is {self.age} years old")

ob = Person()
ob.displayPerson()