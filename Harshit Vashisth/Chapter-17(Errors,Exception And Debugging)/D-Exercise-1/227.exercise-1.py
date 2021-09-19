def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError:
        print('Number must be int or floats')
    except:
        print('Unexpected error')
print(divide(4,2))
print(divide(4,0))
print(divide('4',2))
