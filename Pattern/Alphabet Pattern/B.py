n=int(input())
for i in range(n):
    if i in [0,n//2,n-1]:
        print("* "*(n//2))
    else:
        print("*"+" "*(n-2)+"*")