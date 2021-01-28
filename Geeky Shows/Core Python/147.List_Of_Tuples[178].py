a=[10,20,(30,40)]
print("Original List A:",a)
print(id(a))
print(type(a))
# Appending a new Tuple
a.append((50,60))
print("After Appending A Tuple A:",a)
print(id(a))
print(type(a))
# Accessing List of Tuple using for loop
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
b=[(10,20),(30,40)]
print("Original List B:",b)
print(id(b))
print(type(b))
# Accessing List of Tuple using for loop
n=len(b)
for i in range(n):
    for j in range(len(b[i])):
        print(i,j,b[i][j])
    print()
b.append((50,60))
print("After Appending A Tuple B:",b)
print(id(b))
b.append([50,60])
print("After Appending A List B:",b)
print(id(b))
b.append(10)
print("After Appending A Integer B:",b)
print(id(b))