# method overriding
# isinstance() method
# issubclass() method
class Phone:    # base class / parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"
class Smartphone(Phone):    # derived class / child class level 1
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def full_name(self):
       return f"{self.brand} {self.model_name} and price is {oneplus._price}"
class Flagship_phone(Smartphone):    # derived class / child class level 2
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and fornt camera is {self.front_camera}"
phone=Phone('Nokia','1100',1000)
oneplus=Smartphone('OnePlus','7pro',52000,'8GB','256GB','12MP+20MP+5MP')
samsung=Flagship_phone('Samsung','S10+',60000,'8GB','512GB','12MP+20MP+13MP','8MP')
print(phone.full_name())
print(oneplus.full_name())
print(samsung.full_name())
print(isinstance(oneplus,Smartphone))
print(isinstance(samsung,Smartphone))
print(isinstance(samsung,Phone))
print(isinstance(oneplus,Flagship_phone))
print(issubclass(Smartphone,Phone))
print(issubclass(Smartphone,Flagship_phone))