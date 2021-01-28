# Variable Length Araguments
def show(*num):
    print(num)
    print(num[0])
    print(num[1])
    print(num[2])
show(1,2,3,4,5,6)
def add1(*num):
    z=num[0]+num[1]
    print("Addition:",z)
add1(1,2)
def add2(x,*num):
    z=x+num[0]+num[1]
    print("Addition:",z)
add2(1,2,3)