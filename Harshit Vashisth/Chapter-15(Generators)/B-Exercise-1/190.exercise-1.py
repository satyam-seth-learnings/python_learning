def even_generator(n):
    for num in range(1,n+1):
        if num%2==0:
            yield(num)
even_nums=even_generator(20)
# looping in even_generator function output
for num in even_generator(20):
    print(num)
for num in even_generator(20):
    print(num)
# looping in even_nums generator object
for num in even_nums:
    print(num)
for num in even_nums:
    print(num)
# by adding steps in range function
def even_generator2(n):
    for num in range(1,n+1,2):
        yield(num)
even_nums2=even_generator(20)
for num in even_nums2:
    print(num)