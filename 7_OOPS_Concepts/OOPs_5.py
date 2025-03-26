# 3. Multiple Inheritance :  Base1,Base2 -> Derived (when a child inherits attributes of multiple classes)

class A:
    varA ="Welcome to class A"

class B:
    varB ="Welcome to class B"

class C(A,B):                  # muliple inheritance
    varC = "welcome to class C"

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

