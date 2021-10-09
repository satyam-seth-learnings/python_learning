n=int(input())
for i in range(n):
    if i in (0,n-1):
        print("* "*n)
    else:
        print(" "*2*(n-i-1)+"*")