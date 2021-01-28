# Instance Method Without Parameter
class Mobile:
    # Instance Method
    def show_model(self):
        print('RealMe X')
realme=Mobile()
realme.show_model()
class Mobile1:
    def __init__(self):
        self.model='RealMe X'   # Instance Variable
    # Instance Method
    def show_model(self):
        print('Model:',self.model)
realme1=Mobile1()
realme1.show_model()
# Instance Method Without Parameter
class Mobile2:
    def __init__(self):
        self.model='RealMe X'   # Instance Variable
    # Instance Method
    def show_model(self,p):
        self.price=p
        print('Model:',self.model,'Price:',self.price)
realme2=Mobile2()
realme2.show_model(1000)
redmi2=Mobile2()
redmi2.show_model(1200)