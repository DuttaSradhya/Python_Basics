# Recursion: When a function call itself repeatedly : like a loop : no explicit calling statement from outside
# calling statement is present inside

def show(n):
    if( n==0 ):     # base case : here the loops stops : stopping condition
        return      # returns the control
    print(n)
    show(n-1)     # recursion : show function is called from show function itself
show(5)


def fact(num):
    if(num ==1 or num ==0):
        return 1
    return fact(num-1) * num
print(fact(6))