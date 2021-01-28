stu={101:'Rahul',102:'Raj',103:'Sonam'}
print("Original Dict:")
print(stu)
it=stu.items()
print(it)
print(type(it))
lst=list(it)
print(lst)
print(type(lst))
print(lst[0])
print(lst[0][0])
print(lst[0][1])
for r in lst:
    for c in r:
        print(c)