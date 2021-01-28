from numpy import *
a=zeros((3,2))
print(a)
a1=zeros((3,2),dtype=int)
print(a1)
print(a[0][0])
print(a1[0][0])
for r in a1:
    for c in r:
        print(c)
    print()
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print('Index',i,j,"=",a[i])
    print()
n1=len(a1)
i=0
while i<n:
    j=0
    while j<len(a1[i]):
        print('Index',i,j,"=",a1[i])
        j+=1
    i+=1
    print()