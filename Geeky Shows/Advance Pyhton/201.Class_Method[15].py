# Class Method Without Parameter
# Example-1
class Mobile:
    @classmethod    # Decorator
    def show_model(cls):    # Class Method
        print('Realme X')
realme=Mobile()
Mobile.show_model() # Calling Class Method
# Example-2
class Mobile1:
    fp='Yes'    # Class Variable
    @classmethod    # Decorator
    def show_model(cls):    # Class Method
        print('Fingerprint:',cls.fp)
realme1=Mobile1()
Mobile1.show_model() # Calling Class Method
# Class Method With Parameter
class Mobile2:
    fp='Yes'    # Class Variable
    @classmethod    # Decorator
    def show_model(cls,r):    # Class Method
        cls.ram=r
        print('Fingerprint:',cls.fp)
        print('Ram:',cls.ram)
realme2=Mobile2()
Mobile2.show_model('4GB') # Calling Class Method
