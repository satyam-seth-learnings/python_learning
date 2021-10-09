n=int(input())
for i in range(n):
    if i in (0,n-1):
        print("* "*n)
    elif i==n//2:
        print("* "*(n//2+1))
    else:
        print("*")