class Laptop:
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_name=model
        self.price=price
        self.full_name=brand+' '+model
lap1=Laptop("Asus","Zenbook",45699)
lap2=Laptop("Lenovo","Yogabook",53999)
print(lap1.full_name)
print(lap2.full_name)
print(lap1.price)
print(lap2.price)