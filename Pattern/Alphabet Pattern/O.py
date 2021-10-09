n=int(input())
for i in range(n):
    if i in (0,n-1):
        print(" *"*(n-2))
    else:
        print("*"+" "*(2*(n-2)-1)+"*")