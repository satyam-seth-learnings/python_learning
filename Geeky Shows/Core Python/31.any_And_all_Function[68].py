from numpy import *
a=array([101,102,103,104])
b=array([100,102,106,105])
result=(a==b)
print(result)
print(any(result))
print(all(result))