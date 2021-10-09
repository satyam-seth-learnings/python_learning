n=int(input())
for i in range(n+1):
    if i in (0,n-1):
        print(" *"*(n-2))
    elif i==n-2:
        print("*"+" "*(2*(n-2)-3)+"* *")
    elif i==n:
        print(" "*2*(n-2)+"*")
    else:
        print("*"+" "*(2*(n-2)-1)+"*")