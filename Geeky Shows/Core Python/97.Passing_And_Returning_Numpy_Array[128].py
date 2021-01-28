from numpy import *
def show(arr):
    print("Passed Array arr:",arr)
    print(type(arr))
    for i in arr:
        print(i)
    return arr
print()
a=array([101,102,103,104])
y=show(a)
print("Returning Array Y:",y)
print(type(y))
for i in y:
    print(i)