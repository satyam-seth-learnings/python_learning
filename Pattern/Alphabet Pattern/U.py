n=int(input())
for i in range(n):
    if i==n-1:
        print(" *"*n)
    else:
        print("*"+" "*(2*n-1)+"*")