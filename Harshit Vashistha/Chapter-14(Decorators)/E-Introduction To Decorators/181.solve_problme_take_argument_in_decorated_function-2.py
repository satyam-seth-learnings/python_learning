def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('this is awesome function')
        any_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def func(a):
    print(f'this is function {a}')
func(7)
@decorator_function
def add(a,b):
    return a+b
print(add(2,3))