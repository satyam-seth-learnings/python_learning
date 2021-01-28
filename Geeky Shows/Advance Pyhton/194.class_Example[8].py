# Example-1
class Myclass1(object):
    def show(self):
        print('I am a Method-1')
x=Myclass1()
x.show()
# Example-2
class Myclass2:
    def show(self):
        print('I am a Method-2')
y=Myclass2()
y.show()
# Example-3
class Mobile1:
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print('Model:',self.model)
realme1=Mobile1()
realme1.show_model()
print(realme1.model)
realme1.model='RealMe Pro2'
print(realme1.model)
realme1.show_model()
# Example-3
class Mobile2:
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        price=1000
        print('Model:',self.model,'Price:',price)
realme2=Mobile2()
realme2.show_model()
# Example-4
class Mobile3:
    def __init__(self,m):
        self.model=m
    def show_model(self,p):
        price=p
        print('Model:',self.model,'Price:',price)
realme3=Mobile3('RealMe X')
realme3.show_model(14999)
# Example-5
class Mobile4:
    def __init__(self,m):
        self.model=m
    def show_model(self,p):
        self.price=p
        print('Model:',self.model,'Price:',self.price)
realme4=Mobile4('RealMe X')
realme4.show_model(13999)
print(id(realme4))
redmi=Mobile4('Redmi 7s')
redmi.show_model(2000)
print(id(redmi))
redmi1=Mobile4('Redmi 7s')
redmi1.show_model(2000)
print(id(redmi1))