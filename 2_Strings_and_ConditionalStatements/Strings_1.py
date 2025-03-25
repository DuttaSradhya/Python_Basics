# String is a datatype that stores a sequence of characters
# Basic Operation :
# 1. Concatenation: "hello" + "world" --> "hellowordl"
# 2. length of str: len(str)

str1 = "This is a Sradhya's practice code. \n this should come in next line "   #mostly used where you can use apostrophe s
str2 = '\n My name is Sradhya \t this should come after a tab' 
str3 = """this is a string"""
str4 = "Sradhya"
str5 = "Dutta"
print(str1, str2)

print(str4 + str5) # concatenates string

print(len(str4)) # prints character of string

str6=str4+ " " +str5
print(str6)
print(len(str6))


# Indexing - S R A D H Y A D U T T  A
#            0 1 2 3 4 5 6 7 8 9 10 11
# str="Sradhya_Dutta" , str[0]='A'
# cannot replace letters of a string with help of char str[0]='D' x not possible
# string item does not support item assignment: cannot support manipulation or modifcation

str="Sradhya_dutta"
print(str[0])