#Create a class to create and add Complex Nos

# Operators & Dunder Function
# a + b : addition   a _ _add_ _ (b)
# a - b : addition   a _ _sub_ _ (b)
# a * b : addition   a _ _mul_ _ (b)
# a / b : addition   a _ _truediv_ _ (b)
# a % b : addition   a _ _mod_ _ (b)

class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real, "i +" ,self.img, "j")

    def __add__(self, num2):   #dunder function
        newReal= self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):   #dunder function
        newReal= self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(2,4)
num2.showNumber()

# num3 = num1.add(num2)
num3= num1+num2
num4= num1-num2
num3.showNumber()
num4.showNumber()

