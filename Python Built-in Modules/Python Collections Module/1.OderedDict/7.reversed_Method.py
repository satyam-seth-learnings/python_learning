from collections import OrderedDict
nums=OrderedDict()
nums['one']=1
nums['two']=2
nums['three']=3
nums['four']=4
nums['five']=5
print(nums)
print('Reversed Keys:')
for key in reversed(nums.keys()):
    print(key)
print('Reversed Values:')
for values in reversed(nums.values()):
    print(values)
print('Reversed Items:')
for key,values in reversed(nums.items()):
    print(key,values)