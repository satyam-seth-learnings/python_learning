from collections import OrderedDict
nums=OrderedDict()
nums['one']=1
nums['two']=2
nums['three']=3
nums['four']=4
nums['five']=5
print(nums)
print(nums.popitem())
print(nums)
print(nums.popitem(last=True))
print(nums)
print(nums.popitem(last=False))
print(nums)