n=int(input())
for i in range(n):
    if i==0:
        print(" "*(n-i)+"*")
    elif i==(n//2):
        print(" "*(n-i-1)+"*"+" *"*i+" *")
        continue
    print(" "*(n-i-1)+"*",end=" ")
    print(" "*(2*i)+"*")