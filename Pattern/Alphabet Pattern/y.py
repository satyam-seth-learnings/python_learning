n=int(input())
for i in range(n):
        if i<n//2:
            print(" "*i+"*"+" "*(2*(n//2-i)-1)+"*")
        else:
            print(' '*(n//2)+'*')