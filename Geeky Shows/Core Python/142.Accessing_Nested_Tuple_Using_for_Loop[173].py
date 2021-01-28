a=(10,20,30,(50,60))
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
b=((10,20,30),(40,50,60))
# Without index
for r in b:
    for c in r:
        print(c)
    print()
# With index
n=len(b)
for i in range(n):
    for j in range(len(b[i])):
        print(i,j,b[i][j])
    print()