numbers1=[2,4,3,5,6]
numbers2=[2,6,8,10]
evens1=[]
evens2=[]
for num in numbers1:
    evens1.append(num%2==0)
print(evens1)
print(all(evens1))
print(any(evens1))
for num in numbers2:
    evens2.append(num%2==0)
print(evens2)
print(all(evens2))
print(any(evens2))
# using list comprehension
print(all([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers2]))
print(any([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers2]))