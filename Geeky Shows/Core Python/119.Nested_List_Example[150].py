a=[10,20,30,[50,60]]
print(a[0])
print(a[3][0])
print(a[3])
print("Before Modification A:",a)
a[1]=100
a[3][0]=5
print("After Modification A:",a)
b=[50,60]
c=[10,20,30,b]
print("C:",c)
print("B:",b)
print(c[0])
print(c[3][0])
print(c[3])
print("Before Modification C:",c)
c[1]=100
c[3][0]=70
print("After Modification C:",c)
d=[[10,20,30],[40,50,60]]
print("D:",d)
print("d[0]:",d[0])
print("d[1]:",d[1])
print("d[0][0]:",d[0][0])
print("Before Modification D:",d)
d[0][1]=80
d[1][0]=70
print("After Modification D:",d)