n=int(input())
for i in range(0,n):
    if i==0:
        print(" *"*n)
    elif i==n//2:
        print("*"+" "*(n)+"* "*(n//2))
    elif i in range(n//2+1,n-1):
        print("*"+" "*(n-1)+"*"+" "*(n-1)+"*")
    elif i==n-1:
        print(" *"*(n//2)+" "*n+"*")
    else:
        print("*")