# filter() function
def is_even(a):
    return a%2==0
numbers=[3,4,2,1,5,6,9,8,10]
evens=tuple(filter(is_even,numbers))
print(evens)
even=tuple(filter(lambda a:a%2==0,numbers))
even2=(filter(lambda a:a%2==0,numbers))
print(evens)
for i in even2:
    print(i)
for i in even2:
    print(i)
for i in even:
    print(i)
for i in even:
    print(i)
# using list comprehension
new_evens=[i for i in numbers if i%2==0]
print(new_evens)
print(evens)
print(list(evens))