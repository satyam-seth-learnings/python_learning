# *args as a argument
def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
nums=[2,3,4]
nums1=(2,3,5)
print(multiply_nums(nums))
print(multiply_nums(nums1))
print(multiply_nums(*nums))     #unpack
print(multiply_nums(*nums1))    #unpack