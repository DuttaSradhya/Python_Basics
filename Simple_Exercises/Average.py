# Create Student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average

#Sol1:
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def calc_average(self):
        average=(self.marks1 + self.marks2 + self.marks3)/3
        print("Average of 3 subjects is", average)
    
s1 = Student("Sradhya", 90, 99, 100)
s1.calc_average()



#Sol2:
class Student1:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def calc_average(self):
        sum=0
        for val in self.marks:
            sum += val
        average= sum/3
        print("Hi", self.name, "Your average score is", average)
    
s2 = Student1("Sradhya", [80, 90, 90])
s2.calc_average()
