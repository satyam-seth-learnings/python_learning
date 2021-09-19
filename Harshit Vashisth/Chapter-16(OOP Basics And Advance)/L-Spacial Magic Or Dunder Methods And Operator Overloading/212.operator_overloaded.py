# Operator Overloading
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def __add__(self,other):
        return self.price+other.price
my_phone=Phone('Nokia','1100',1000)
my_phone2=Phone('JIO','Jio Phone',1500)
print(my_phone+my_phone2)
print(3+5)