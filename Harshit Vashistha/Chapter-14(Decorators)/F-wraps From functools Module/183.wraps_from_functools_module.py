# wraps From functools Module
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)    #_skip this line_
    def wrapper_function(*args,**kwargs):
        """ this is wrapper function """
        print('this is awesome function')
        return any_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def add(a,b):
    ''' this is add funcion '''
    return a+b
print(add.__doc__)
print(add.__name__)