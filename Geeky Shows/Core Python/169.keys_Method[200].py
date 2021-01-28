stu={101:'Rahul',102:'Raj',103:'Sonam'}
print("Original Dict:")
print(stu)
all_keys=stu.keys()
print(all_keys)
print(type(all_keys))
keys_lst=list(all_keys)
print(keys_lst)
print(type(keys_lst))
print(keys_lst[0])
for k in keys_lst:
    print(k)