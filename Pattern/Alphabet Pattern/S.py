n=int(input())
for i in range(n):
    if i in (0,n//2,n-1):
        print(" *"*(n//2))
    elif i<n//2:
        print("*")
    else:
        print(" "*n+"*")