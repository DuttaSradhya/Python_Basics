# Slicing : Accessing parts of a String  = str [ starting_idx : ending_idx] here the element of ending index is not included
# str="SradhyaDutta"
# str[ 1 : 4] is "rad"
# str[ : 4] is same as str[ 0 : 4]
# str[ 1 : ] is same as str[ 1 : len(str)]

str="SradhyaDutta"
print(str[ 1 : 4])  # takes 1th, 2nd and 3rd. Does not take 4th elem
print(str[ : 4])    # prints from 0 index
print(str[ 1 : ])   # prints till last endex

# Slicing : Case 2 : Negative Index: This feature is not available in Java or C++
#  A  P  P  L  E
# -5 -4 -3 -2 -1
# Backward counting starts from -1 to -2 ....

st="Apple"
print(st[ -3: -1])
print(st[ -3: ])
print(st[ : -1])
print(st[ : ])     #  prints Apple