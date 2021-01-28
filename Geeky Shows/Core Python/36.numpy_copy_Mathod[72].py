from numpy import *
a=array([101,102,103,104])
b=a.copy()
print(a)
print(b)
print(id(a))
print(id(b))
a[2]=100
print(a)
print(b)
print(id(a))
print(id(b))