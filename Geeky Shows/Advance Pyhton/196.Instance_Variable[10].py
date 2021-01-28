class Mobile:
    def __init__(self):
        self.model='Realme X'   # Instance Variable
    def show_model(self):
        print(self.model)   #   Accessing Instance Variable
realme=Mobile()
redmi=Mobile()
geek=Mobile()
print(realme.model)
print(redmi.model)
print(geek.model)
redmi.model='Redmi 7s'
print(realme.model)
print(redmi.model)
print(geek.model)