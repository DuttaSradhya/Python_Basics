# Create a class called Order which stores item and its price
# Use Dunder function --gt--() to convey that
#  order 1 > order 2 if price of order 1 > price of order 2

class Order:

    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price > order2.price    

order1=Order("chips", 20)
order2=Order("tea", 4)
print(order1 > order2)   #returns true when price of order 1 is greated than order 2
