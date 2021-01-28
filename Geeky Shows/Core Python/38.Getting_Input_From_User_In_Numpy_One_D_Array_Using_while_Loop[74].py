from numpy import *
n=int(input("Enter The Number Of Elements:"))
a=zeros(n,dtype=int)
i=0
while i<n:
    a[i]=int(input("Enter Element:"))
    i+=1
j=0
while j<n:
    print(a[j])
    j+=1