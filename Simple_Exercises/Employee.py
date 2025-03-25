# Define a Employee class with attributes role, department & salary. This class also has a showDetails method
# Create an Engineer class that inherits properties from Employee & has additional attributes name and age

class Employee:
    def __init__(self, role, dept, sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    
    def showDetails(self):
        print("Details of Employee Designation :" , self.role , "Role", self.dept , "Department" , self.sal , "Euro")

e1 = Employee("QA", "TECH", "60000")
e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Enginner", "IT", "75000")

    def showDetailsnow(self):
        print("Name : " ,self.name, "Age : " ,self.age, "Role : " ,self.role, "Dept : " ,self.dept, "Salary : " ,self.sal) 

e2=Engineer("Sradhya Dutta", 24)    
e2.showDetailsnow()       