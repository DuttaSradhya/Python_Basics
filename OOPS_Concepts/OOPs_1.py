# Abstraction = Hiding th eimplementation details of a class and only showing the essential features to the user
# Encapsulation = Wrapping data(attributes)  and functions(methods) into a single unit (Object).

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")

car1=Car()
car1.start() 

car2=Car()
car2.start()

# All unnecessary implementation details have been hidden inside the class.
# Only the essential features (last 2 lines outside class) shown to the user

del car2 #using del keyword deletes an object or object properties (attributes)