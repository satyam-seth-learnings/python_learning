n=int(input())
for i in range(n):
        if i==0 or i==n-1:
            print("* "*(n//2))
        else:
            print(" "*(n//2-1)+"*")