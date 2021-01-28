from numpy import *
m=int(input("Enter Number Of Rows:"))
n=int(input("Enter Number Of Columns:"))
a=zeros((m,n),dtype=int)
u=len(a)
print(a)
for i in range(u):
    for j in range(len(a[i])):
        a[i][j]=int(input("Enter Element:"))
for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
print(a)
for r in a:
    for c in r:
        print(c)
