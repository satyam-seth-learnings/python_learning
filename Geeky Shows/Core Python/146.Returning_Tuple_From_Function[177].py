def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t
tup=(10,20.5,-30,"Satyam")
new_tup=show(tup)
print(new_tup)
