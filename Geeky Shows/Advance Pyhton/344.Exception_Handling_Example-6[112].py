a=10
b=0 #Or b=5
try:
    c=a/b
    print(c)    #Or print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as ob:
    print(ob)
print('Rest Of The Code')