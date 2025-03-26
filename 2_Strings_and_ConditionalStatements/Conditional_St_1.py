#if-elif-else Statements
# Ex 1: Voting Age
age=int(input("Enter your age: "))
if (age>=18):
    print("You can vote")
else:
    print("You cannot vote")    

# Nested-if-else 
age1=17
if(age1>=18):
    print("can drive")
    if(age1>=34):
        print("can run")
    else:
        print("cannot run") 
else:
    print("Cannot drive")            

# Ex 2: Traffic Signal
light=input("Enter your colour : ")
if (light == "red"):
    print("stop")
elif(light == "green"):
    print("go")    
elif(light == "yellow"):
    print("pause and look")        
else:
    print("Light is broken")    
print("End of code")    

# Ex 3: F=Grade Students based on marks
#  marks >=90, gradee="A"
#  90 > marks >=80, grade="B"
#  80 > marks >= 70, grade="C"
#  70 > marks , grade="D"
marks=90
if (marks >= 90):
    print("A")
elif (marks >=80 and marks<90):
    print("B")
elif (marks >=70 and marks<80):
    print("C")
else:
    print("D")    
 

