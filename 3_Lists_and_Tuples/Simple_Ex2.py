# WAP to check if a list contains a palindrome of elements (Hint: use copy() method)
# [1,2,3,2,1] [1,"abc", "abc", 1]

marks=[1,2,3,2,1]
marks_copy= marks.copy()
marks_copy.reverse()
if (marks_copy == marks):
    print("Palindrome elements")
else:
    print("Not Palindrome elements")    

# WAP to count the no of students with "A" grade in the followingg tuple
# ["C", "D", "A", "A", "B", "B", "A"]
# Store the above values in a list & sort them from "A" to "D"

grades=("C", "D", "A", "A", "B", "B", "A")
print(grades)
print('Count of Grade "A" is ', grades.count("A"))

gradelist=list(grades)
gradelist.sort()
print(gradelist)