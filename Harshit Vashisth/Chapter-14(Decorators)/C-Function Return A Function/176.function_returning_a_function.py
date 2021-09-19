# function returning a function
def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func
var=outer_func()
var()
def outer_func2():
    def inner_func2():
        print('inside inner func')
    return inner_func2()
def outer_func3(msg):
    def inner_func3():
        print(f'message is {msg}')
    return inner_func3
var3=outer_func3("hello there!")
var3()