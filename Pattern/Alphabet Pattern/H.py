n=int(input())
for i in range(n):
    if i==n//2:
        print("* "*n)
    else:
        print("*"+" "*(2*n-3)+"*")