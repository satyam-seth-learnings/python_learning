def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('Oops you are passing worng data type to function')
print(add(2,3))
print(add(2,'one'))