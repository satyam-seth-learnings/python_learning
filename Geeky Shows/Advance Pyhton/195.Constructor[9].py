class Mobile:
    def  __init__(self):
        print("Mobile Constructor Called")
realme=Mobile()
redmi=Mobile()
class Mobile1:
    # Constructor Without Parameter
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print('Model:',self.model)
realme=Mobile1()
realme.show_model()
class Mobile2:
    # Constructor With Parameter
    def __init__(self,m,v=80):
        self.model=m
        self.volume=v
    def show_model(self,p):
        price=p     #   Local Variable
        print('Model:',self.model,'And Price:',price)
        print('Volume:',self.volume)
# Passing Arguments To Constructor
realme1=Mobile2('RealMe X')
# Accessing Method From Outside Class
realme1.show_model(1000)
realme2=Mobile2('Redmi 7s',50)
realme2.show_model(1200)
