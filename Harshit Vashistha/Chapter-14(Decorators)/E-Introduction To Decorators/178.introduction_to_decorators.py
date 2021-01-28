# introduction to decorators
def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function
def func1():
    print('this is function 1')
def func2():
    print('this is function 2')
var=decorator_function(func1)
var()
func2=decorator_function(func2)
func2()