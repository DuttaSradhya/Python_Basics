# Super Methods: super() method to access methods of the parent class: soper=parent

class Car:                          # parent class
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")    

class ToyotaCar(Car):               # child class of Car
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name=name
        

car1= ToyotaCar("prius", "electic")
print(car1.type)        
car1.start()

