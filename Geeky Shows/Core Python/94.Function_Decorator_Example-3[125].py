def decor1(num):
    def inner():
        b=num()
        multi=b*5
        return multi
    return inner
def decor2(num):
    def inner():
        a=num()
        add=a+5
        return add
    return inner
def num():
    return 10
print(num())
num=decor2(decor1(num))
print(num())