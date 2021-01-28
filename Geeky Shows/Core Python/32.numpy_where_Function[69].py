from numpy import *
a=array([101,102,103,104])
b=array([100,108,103,104])
result=where(a>b,a,b)
print(result)