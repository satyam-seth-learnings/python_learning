class Laptop:
    discount_percent=10
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_name=model
        self.price=price
    def apply_discount(self):
        off_price=(Laptop.discount_percent/100)*self.price
        return self.price-off_price
#	Laptop.discount_percent=0
lap1=Laptop("Asus","Zenbook",45699)
lap2=Laptop("Lenovo","Yogabook",53999)
print(lap1.apply_discount())
print(lap2.apply_discount())