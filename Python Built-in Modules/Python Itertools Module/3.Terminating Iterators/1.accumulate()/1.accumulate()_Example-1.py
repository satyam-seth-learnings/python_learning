from itertools import accumulate
l=[1,2,3,4,5]
result1=accumulate(l)
print('Result 1:')
for each in result1:
    print(each)
result2=accumulate(l,initial=100)
print('Result 2:')
for each in result2:
    print(each)