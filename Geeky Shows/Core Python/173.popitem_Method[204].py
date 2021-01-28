stu={101:'Rahul',102:'Raj',103:'Sonam'}
print("Original Dict:")
print(stu)
print(id(stu))
removed_item=stu.popitem()
print("Afetr Removing Dict:")
print(stu)
print(id(stu))
print("Remove Value:",removed_item)