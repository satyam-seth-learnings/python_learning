# polymorphism
class Phone():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def phone_name(self):
        return f"{self.brand} {self.model}"
    def __len__(self):
        return len(self.phone_name())
class Smartphone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera=camera
    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    def __len__(self):
        return self.price
phone=Phone('Nokia','1100',1000)
smartphone=Smartphone('OnePlus','7Pro',52000,'16MP')
print(phone.phone_name())
print(smartphone.phone_name())
print(len(phone))
print(len(smartphone))