stu={101:'Satyam',102:'Ram'}
print("Original Dict:")
print(stu)
print(id(stu))
new_stu=stu.copy()
print("Copied Dict:")
print(new_stu)
print(id(new_stu))
stu[102]='Python'
print(stu)
print(new_stu)