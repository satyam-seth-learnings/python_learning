# Class Variable- Namespace
class Mobile:
    fp='Yes'    # Class Variable
    @classmethod
    def is_fp(cls): # Class Method
        print('Finger Print:',cls.fp)   # Accessing Class Variable
realme=Mobile()
redmi=Mobile()
geek=Mobile()
print('Class FP:',Mobile.fp)
print('RealMe:',realme.fp)
print('Redmi:',redmi.fp)
print('Geek:',geek.fp)
Mobile.fp='No'
print('Class FP:',Mobile.fp)
print('RealMe:',realme.fp)
print('Redmi:',redmi.fp)
print('Geek:',geek.fp)
realme.fp='Not Working'
print('Class FP:',Mobile.fp)
print('RealMe:',realme.fp)
print('Redmi:',redmi.fp)
print('Geek:',geek.fp)