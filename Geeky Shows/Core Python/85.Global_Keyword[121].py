a=50
i=0
def show1():
    a=10
    print("A:",a)
show1()
print("A:",a)
def show2():
    i=0
    i+=1
    print("I:",i)
show2()
print("I:",i)
def show3():
    global i
    i+=1
    print("I:",i)
show3()
print("I:",i)