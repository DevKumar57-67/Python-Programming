# A Class in python is a blueprint for creating objects, which holds data and methods that operate on the data.



class Myclass:
    def __init__(self, name,age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = int(input("Enter your age: "))
obj = Myclass(name, age)
print("Name:", obj.name, "Age:", obj.age)

