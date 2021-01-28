def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    return c
print(greatest(100,200,3000))