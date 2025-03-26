# Inheritance: When one class (child/derived) derives the properties & methods of another class (parent/base)

# Inheritance Types
# 1. Single Inheritance        : Base -> Child
# 2. Multi-level Inheritance   : Base -> Derived -> Next Derived
# 3. Multiple Inheritance      : Base1, Base2 -> Derived Class (when a child inherits attributes of multiple classes)

class Car:                          # parent class
    color="red"

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")    

class ToyotaCar(Car):               # child class
    def __init__(self,name):
        self.name=name

car1= ToyotaCar("fortuner")
car2= ToyotaCar("prius")

car1.start()  #object of Child class can use attributes and methods of Parent class
print(car1.color)

