def val(x):
    print(x,id(x))
    x=15
    print(x,id(x))
x=10
val(x)
print(x,id(x))