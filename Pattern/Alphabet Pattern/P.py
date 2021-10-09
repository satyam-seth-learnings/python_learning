n=int(input())
for i in range(n):
    if i in (0,n//2):
        print("* "*(n//2))
    elif i>0 and i<n//2:
        print("*"+" "*(n-2)+"*")
    else:
        print("*")