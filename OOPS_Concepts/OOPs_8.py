class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths= maths

        # percantage attribute
        self.percentage = ((self.phy + self.chem + self.maths)/3) + "%"

stu1=Student(50, 40, 50)
print(stu1.percentage)

# Property: We use @property decorator on any method in the class to use the method as a property

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths= maths

    @property
    def calc_percentage(self):
        self.percentage = ((self.phy + self.chem + self.maths)/3) + "%"

stu1=Student(50, 40, 50)
print(stu1.percentage)

stu1.phy= 86    # when marks of physics is changed percentage also gets updated
print(stu1.percentage)

