# generator function
# example
def nums(n):
    for i in range(1,n+1):
        print(i)
nums(10)
# generator
def nums2(n):
    for i in range(1,n+1):
        yield i
print(nums2(10))
numbers=nums2(10)
for num in numbers:
    print(num)
for num in numbers:
    print(num)
# after generator converted into list
numbers=list(nums2(10))
for num in numbers:
    print(num)
for num in numbers:
    print(num)