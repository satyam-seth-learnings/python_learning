# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.__model_name=model_name    #   name mangling
        self._price=price   #   private instance veriable
    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ...")
    def full_name(self):
        return f"{self.brand} {self.model_name}"
l=[3,4,1,2]
l.sort()       # tim sort
print(l)
phone1=Phone('nokia','1100',1000)
print(phone1._price)
phone1._price=-1000
print(phone1._price)
# print(phone1.__model_name)
print(phone1.__dict__)
print(phone1._Phone__model_name)
phone1._Phone__model_name=-1122
print(phone1._Phone__model_name) 