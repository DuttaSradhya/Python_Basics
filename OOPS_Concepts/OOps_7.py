# Class Method : A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method cant access or modify class state & generally for utility; statis methods does not use any attribute

# class Student:
#     @classmethod #decorator
#     def college(cls):
#         pass

class Person:
    name="anonymous"

    def changeName(self, name):
        self.name=name

p = Person()
p.changeName("Sradhya")
print(p.name)
print(Person.name)



class Person1:
    name1="anonymous"

    # def changeName1(self, name1):
    #     Person1.name1=name1       # change class name

    @classmethod
    def changeName1(cls, name1):
        cls.name1=name1

p1 = Person1()
p1.changeName1("Sradhya")
print(p1.name1)
print(Person1.name1)


# 3 types of methods: 
# static methods: no access to class or instance methods
# class methods            : cls, clas comes as an argument : use only class attributes
# instance methods (normal): self : self comes as an argument : use only instance attributes