stu={101:'Rahul',102:'Raj',103:'Sonam'}
print("Original Dict:")
print(stu)
print(id(stu))
stu.update({104:'Python'})
print("Update Dict:")
print(stu)
print(id(stu))
vals={'Name':'Satyam','Age':20,'Gender':'Male'}
stu.update(vals)
print("Update Dict:")
print(stu)
print(id(stu))