# Keyword Variable Length Arguments
def add1(**num):
    z=num['a']+num['b']+num['c']
    print("Addition:",z)
add1(a=5,b=2,c=4)
def add2(x,**num):
    print(num)
    z=x+num['a']+num['b']
    print("Addition:",z)
add2(3,a=5,b=2)
add2(3,a=5,b=2,c=12)