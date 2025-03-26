# WAP to print the length of a list (list is the parameter)
def calc_List_Len(li):
    print(len(li))

nums=[1,2,3,4]
cities =["Dresden", "Wuppertal", "Essen", "Dortmund"]
heroes =["Thor", "Ironman", "Captain America"]

calc_List_Len(nums)
calc_List_Len(cities)
calc_List_Len(heroes)

# WAP to print the elements of a list in a single line (list is the parameter)
# print(heroes[0], end=" ")
# print(heroes[1], end=" ")

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()   # now no extra % will come


# WAP to find the factorial of n ( n is the parameter)
def calc_Fac(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
    print(fact)    
calc_Fac(5)


# WAP to convert USD to INR
def coverter(usd_val):
    inr_val=usd_val*83
    print(usd_val, "USD =", inr_val ,"INR" )
coverter(100)

# WAP to check if a no. is odd or even
def checkEvenOdd(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")    
checkEvenOdd(4)        