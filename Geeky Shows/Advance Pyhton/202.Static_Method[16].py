# Satatic Method Without Parameter
class Mobile:
    fp='Yes'
    @staticmethod
    def show_fp():  # Decorator
        print('Fingerprint:',Mobile.fp)
    @staticmethod   # Decorator
    def show_model():   # Static Method
        print('RealMe X')
realme=Mobile()
Mobile.show_fp() # Calling Staic Method
Mobile.show_model() # Calling Staic Method
# Sataic Method With Parameter
class Mobile1:
    @staticmethod   # Decorator
    def show(m,p):  # Static Method
        model=m
        price=p
        print('Model:',model,'Price:',price)
Mobile1.show('Redmi 7s',1000)   # Calling Staic Method