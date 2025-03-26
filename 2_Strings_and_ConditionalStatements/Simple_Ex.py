# WAP to check if a no. enetred by the user is odd or even
number=int(input("Enter a number: "))
if (number%2==0):
    print("Even no")
else:
    print("Odd no") 

# WAP to find the greatest of 3 nos entered by the user 
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if (num1 > num2 and num1> num3):
    print("Greatest no is first no : ", num1)
elif(num2 > num1 and num2> num3):
    print("Greatest no is second no : ", num2)
else:
    print("Greatest no is thid no : ", num3)     

# WAP to check if a no. is multiple of 7 or not
num=49
if (num%7==0):
    print(num, " is a Multiple of 7")
else:
    print(num, "is Not multiple of 7") 