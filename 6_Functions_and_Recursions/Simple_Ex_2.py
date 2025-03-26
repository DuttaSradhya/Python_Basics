# Write a recursive func to print all elements in a list Hint: use list and indes as parameters

def print_list(list, idx):
    if(idx== len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mano", "apple", "litchi" , "banana"]    
print_list(fruits,0)