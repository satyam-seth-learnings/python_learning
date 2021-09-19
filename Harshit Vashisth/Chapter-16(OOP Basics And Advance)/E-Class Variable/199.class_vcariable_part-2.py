class Laptop:
    discount_percent=10
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_name=model
        self.price=price
    def apply_discount(self):
        off_price=(self.discount_percent/100)*self.price
        return self.price-off_price
lap1=Laptop("Asus","Zenbook",45699)
lap2=Laptop("Lenovo","Yogabook",53999)
print(lap1.__dict__)
lap2.discount_percent=50
print(lap2.__dict__)
print(lap2.apply_discount())