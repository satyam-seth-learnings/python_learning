# *args with normal parameter
def multiply_nums(num,*args):
    multiply=1
    print(num)
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multiply_nums(2,2,3))
print(multiply_nums(2))