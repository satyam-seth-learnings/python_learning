from numpy import *
m=int(input("Enter Number Of Rows:"))
n=int(input("Enter Number Of Columns:"))
a=zeros((m,n),dtype=int)
print(a)
u=len(a)
i=0
while (i<u):
    j=0
    while j<len(a[i]):
        a[i][j]=int(input("Enter Element:"))
        j+=1
    i+=1
i=0
while i<u:
    j=0
    while j<len(a[i]):
        print("Index",i,j,"=",a[i][j])
        j+=1
    i+=1
print(a)