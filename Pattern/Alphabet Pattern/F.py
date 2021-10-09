n=int(input())
for i in range(n):
    if i==0:
        print("* "*n)
    elif i==n//2:
        print("* "*(n//2+1))
    else:
        print("*")