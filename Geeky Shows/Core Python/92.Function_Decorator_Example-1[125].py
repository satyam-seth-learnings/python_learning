def decor(fun):
    def inner():
        print("IF: Before enhancing Function")
        fun()
        print("IF: After enhancing Function")
    return inner
def num():
    print("We will use this function")
    print("add will enhance this in decorator")
num()
num=decor(num)
num() 
@decor
def num1():
    print("We will use this function")
    print("add will enhance this in decorator")
num1()