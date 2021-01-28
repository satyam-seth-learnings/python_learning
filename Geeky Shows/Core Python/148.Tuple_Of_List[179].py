a=(10,20,[30,40])
print("Original Tuple A:",a)
print(id(a))
print(type(a))
# Modifying Lists
a[2][0]=90
print("After Modifying Tuple:",a)
print(id(a))
# Accessing Tuple of Lists using for loop
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
b=([10,20],[30,40])
print("Original Tuple B:",b)
print(id(b))
b[0][0]=80
print("After Modification:",b)
print(id(b))
# Accessing Tuple of Lists using for loop
n=len(b)
for i in range(n):
    for j in range(len(b[i])):
        print(i,j,b[i][j])
    print()