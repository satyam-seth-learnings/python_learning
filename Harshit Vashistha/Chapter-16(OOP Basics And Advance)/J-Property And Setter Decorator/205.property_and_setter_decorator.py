# will discuss three problems in existing
# then we will solve them using,setter decorator
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    @property
    def complite_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
phone1=Phone('Nokia','1100',-1000)
print(phone1.brand)
print(phone1.model_name)
phone1.price=-500
print(phone1.price)
print(phone1.complite_specification)