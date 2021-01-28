a=50
def show():
    x=10
    print("Local Variable:",x)
    print("Global Variable:",a)
show()
print("Global Variable:",a)
i=3
def myfun():
    a=i+1
    # i=i+1 -> Error     
    print("My Function:",a)
myfun()