# Define a Circle class to create a circle with radius r using the constructor
# Define an Area() method of the class which calculates the area of the circle
# Define a Perimeter() method of the class which allows you to calculate th eperimeter of the circle

class Circle:
    def __init__(self, r):
        self.radius=r

    def calcArea(self):
        self.area=(22*(self.radius ** 2))/7
        return self.area

    def calcPerimeter(self):
        self.perimeter=(2*22*(self.radius))/7 
        return self.perimeter   
    
c1=Circle(7)
print(c1.calcArea())  
print(c1.calcPerimeter())  