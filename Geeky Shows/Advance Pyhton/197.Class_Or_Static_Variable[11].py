class Mobile:
    fp='Yes'    #    Class Variable
    @classmethod
    def is_fp(cls):
        print(cls.fp)
realme=Mobile()
print(Mobile.fp)
Mobile.is_fp()
class Mobile1:
    fp='Yes'    #    Class Variable
    def __init__(self):
        self.model='RealMe X'   #   Instance Variable
    def show_model(self):
        print('Model:',self.model)  #   Accessing Class Variable
    @classmethod
    def is_fp(cls):     #   Class Method
        print('Finger Print:',cls.fp)       #   Accessing Class Variable
realme1=Mobile1()
realme1.show_model()
Mobile1.is_fp()
Mobile1.fp='No'
Mobile1.is_fp()
class Mobile2:
    fp='Yes'    #    Class Variable
    @classmethod
    def is_fp(cls): #   Class Method
        print('Finger Print:',cls.fp)
realme=Mobile2()
redmi=Mobile2()
geek=Mobile2()
print('RealMe:',Mobile2.fp)
print('Redmi:',Mobile2.fp)
print('Geek:',Mobile2.fp)
Mobile2.fp='No'
print('RealMe:',Mobile2.fp)
print('Redmi:',Mobile2.fp)
print('Geek:',Mobile2.fp)