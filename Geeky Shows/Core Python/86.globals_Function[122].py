a=50
def show1():
    a=10
    print("Local Variable A:",a)
show1()
print("Global Variable A:",a)
def show2():
    print("Local Variable A:",a)
show2()
print("Global Variable A:",a)
# print(globals()['a'])
def show3():
    a=10
    print("Local Variable A:",a)
    x=globals()['a']
    print("Global Variable A:",x)
show3()