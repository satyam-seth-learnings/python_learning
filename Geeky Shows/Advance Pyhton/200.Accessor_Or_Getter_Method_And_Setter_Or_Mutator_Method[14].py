# Instance Method- Accessor Method / Getter Method
class Mobile:
    def __init__(self):
        self.model='RealMe X'   # Instance Varible
    def get_model(self):    # Accessor Method
        return self.model
realme=Mobile()
m=realme.get_model()
print(m)
# Instance Method- Mutator / Setter Method Without Parameter
class Mobile1:
    def __init__(self):     # Instance Variable
        self.model='RealMe X'
    def set_model(self):    # Mutator Method
        self.model='RealMe 2'
realme1=Mobile1()
# Before Setting
print(realme1.model)
# After Setting
realme1.set_model()
print(realme1.model)
# Instance Method- Mutator / Setter Method With Parameter
class Mobile2:
    def set_model(self,m):  # Mutator Method
        self.model=m
realme2=Mobile2()
realme2.set_model('Galaxy S20')
print(realme2.model)