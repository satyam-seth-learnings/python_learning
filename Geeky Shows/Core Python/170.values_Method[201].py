stu={101:'Rahul',102:'Raj',103:'Sonam'}
print("Original Dict:")
print(stu)
all_values=stu.values()
print(all_values)
print(type(all_values))
values_lst=list(all_values)
print(values_lst)
print(type(values_lst))
print(values_lst[0])
for v in values_lst:
    print(v)