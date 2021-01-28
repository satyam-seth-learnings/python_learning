class Laptop:
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_name=model
        self.price=price
    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price-off_price
lap1=Laptop("Asus","Zenbook",45699)
lap2=Laptop("Lenovo","Yogabook",53999)
print(lap1.apply_discount(15))
print(lap2.apply_discount(5))