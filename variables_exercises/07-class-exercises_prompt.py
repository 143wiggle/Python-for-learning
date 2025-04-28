# Exercise: Class with user input
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
print(person.name, person.age)
