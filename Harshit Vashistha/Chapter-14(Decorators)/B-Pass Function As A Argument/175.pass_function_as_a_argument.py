# pass function as a arguments
# using map() function
def square(a):
    return a**2
l=[1,2,3,4,5]
print(list(map(square,l)))
print(list(map(lambda a:a**2,l)))
# by creating our function
def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l))
print(my_map(lambda a:a**3,l))
# using list comprehension
def my_map2(fun,l):
    return [fun(item) for item in l]
print(my_map2(lambda a:a**3,l))