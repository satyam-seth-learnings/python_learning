from numpy import *
n=array([[10,20,30],
        [40,50,60],
        [70,80,90]])
print("Original Array: ")
print(n)
print(n[0])
print(n[1])
print(n[2])
print("0th Row All Columns:")
a=n[0,:]
print(a)
print("1th Row All Columns:")
a1=n[1,:]
print(a1)
print("All Rows 0th Column:")
a2=n[:,0]
print(a2)
for i in a2:
    print(i)
print("All Rows 2nd Column:")
a3=n[:,2]
print(a3)
print(n[0:1,0:1])
print(n[2:3,2:3])
print(n[0:2,1:3])
print(n[0,0])