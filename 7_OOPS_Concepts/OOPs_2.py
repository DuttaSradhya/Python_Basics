#                              Private attributes & methods

# Conceptual Implementations in Python: Private attributes and methods are meant to be used only within the class 
# and are not accessible from outside the class. Done to prevent access of instance attributes outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #private "__"

    def reset_pass(self):
        print(self.__acc_pass)    

acc1=Account("12345","abcde")
print(acc1.acc_no)
#print(acc1.__acc_pass) #private attribute : not accessible outside the class
acc1.reset_pass()

class Person:
    __name="anonymous"  # private attribute

    def __hello(self):      # private method
        print("Hello User!") 

    def welcome(self):
        self.__hello()    # calling another function

p1=Person()
# print(p1.__name) #not possible
# p1.hello() #not possible
p1.welcome()