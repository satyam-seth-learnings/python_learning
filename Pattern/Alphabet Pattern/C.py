n=int(input())
for i in range(0,n):
    if i in (0,n-1):
        print(" *"*(n//2))
    else:
        print("*")