def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function
@decorator_function
def func():
    print('this is function')
func()
# func(7)   Error