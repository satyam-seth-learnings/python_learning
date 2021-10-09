n=int(input())
for i in range(n//2):
    print(" "*2*i+"*"+" "*4*((n//2)-i-1)+"*")
for i in range(n//2):
    print(" "*2*((n//2)-i-1)+"*"+" "*4*i+"*")