from collections import OrderedDict
nums=OrderedDict()
nums['one']=1
nums['two']=2
nums['three']=3
nums['four']=4
nums['five']=5
print(nums)
nums.move_to_end('two')
print(nums)
nums.move_to_end('four',last=False)
print(nums)