from numpy import *
a=array([[10,20,30,40],[50,60,70,80]])
print("Accessing Without Index")
for r in a:
    for c in r:
        print(c)
    print()
a[0][2]=200
a[1][3]=100
print(a[0])    
print(a[1])    
print("Accessing With Index")
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()