def decor(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner
def num():
    return 10
print(num())
result_fun=decor(num)
print(result_fun())
def num1():
    return 11
print(num1())
num1=decor(num1)
print(num1())
@decor
def num2():
    return 20
print(num2())