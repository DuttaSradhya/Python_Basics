# Write a recursive func to calculate the sum of first n natural numbers

def calc_sum(n):
    if(n==0):
        return 0
    print(n)
    return calc_sum(n-1) + n

print(calc_sum(5))
