a=10
b=0 #Or b=5
try:
    c=a/b
    print(c)
    print('Inside Try')
except ZeroDivisionError as obj:
    print(obj)
print('Rest Of The Code')