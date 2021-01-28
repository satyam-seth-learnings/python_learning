# map() function
numbers=[1,2,3,4]
def square(a):
    return a**2
print(map(square,numbers))
squares=list(map(square,numbers))
print(squares)
# with lambda expression
squares2=list(map(lambda a:a**2,numbers))
print(squares2)
# by list comprehension
squares_new=[i**2 for i in numbers]
print(squares_new)
# by append method
new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)