# can we derive more than one class?
class Phone:    # base class / parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"
class Smartphone(Phone):    # derived class / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
class Smartphone2(Phone):    # derived class / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
phone=Phone('Nokia','1100',1000)
smartphone=Smartphone('OnePlus','7pro',52000,'8GB','256GB','12MP+20MP+5MP')
smartphone2=Smartphone2('Samsung','S10+',60000,'8GB','512GB','12MP+20MP+12MP')
print(phone.full_name())
print(smartphone.full_name()+f" and price is {smartphone._price}")
print(smartphone2.full_name()+f" and price is {smartphone2._price}")