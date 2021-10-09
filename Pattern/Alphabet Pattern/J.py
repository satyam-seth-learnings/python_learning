n=int(input())
for i in range(n):
    if i<=n//2:
        print(" "*n+"*")
    elif i>n//2 and i!=n-1:
        print("*"+" "*(n-1)+"*")
    else:
        print(" *"*(n//2))