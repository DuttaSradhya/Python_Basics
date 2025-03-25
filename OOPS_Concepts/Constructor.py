#Constructor & Methods

class Student:
    city="Dresden"           #class attributes
    fullname="anonymous"     #class attributes

    #default constructor                 
    def __init__(self):
        print("default constructor")  

    #parameterized constructor
    def __init__(self, fullname, age):
        self.fullname=fullname     #instance attributes
        self.age=age               #instance attributes
    
    #method welcome
    def welcome(self):
        print("Welcome", self.fullname)

    #method getmarks
    def get_age(self):
        return self.age
    
    @staticmethod
    #self method hello
    def hello():
        print("hello")


s1 = Student("Sradhya", 24)  
s1.welcome()
print(s1.fullname)  
print("Age of Sradhya is:", s1.get_age())  
print(s1.city) 

s2 = Student("Dipayan" , 27)
s2.welcome()
print(s2.fullname) 
print(s2.age)  
print(s2.city) 

#Static Methods
s3 = Student("Dip" , 27)
s3.welcome()
s3.hello()