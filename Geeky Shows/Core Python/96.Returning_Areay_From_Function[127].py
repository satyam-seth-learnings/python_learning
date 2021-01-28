from array import *
def show():
    a=array('i',[101,102,103,104,105])
    return a
y=show()
print("Returning Array Y:",y)
print(type(y))
for i in y:
    print(i)