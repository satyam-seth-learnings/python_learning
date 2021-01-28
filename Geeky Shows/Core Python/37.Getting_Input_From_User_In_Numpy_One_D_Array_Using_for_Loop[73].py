from numpy import *
n=int(input("Enter The Number Of Elements:"))
a=zeros(n,dtype=int)
print(a)
for i in range(n):
    a[i]=int(input("Enter Element:"))
for i in a:
    print(i)