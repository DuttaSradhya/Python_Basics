# 2. Multi-level Inheritance   : Base -> Derived -> Next Derived


class Car:                          # parent class

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")    

class ToyotaCar(Car):               # child class of Car
    def __init__(self,brand):
        self.brand=brand


class Fortuner(ToyotaCar):          # child class of Fortuner Car 
    def __init__(self,type):
        self.type=type

    def print_type(self):
        print("Car Type :",self.type)    

car1=Fortuner("Diesel")   
car1.print_type()          # method of parent class
car1.start()              # method of grand parent class