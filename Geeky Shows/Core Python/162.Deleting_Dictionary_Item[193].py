stu={101:'Satyam',102:'Raj',103:'Ram'}
print("Before Deletion:")
print(stu)
print(id(stu))
del stu[102]
print("After Deletion:")
print(stu)
print(id(stu))
del stu
# print(stu)    NameError: name 'stu' is not defined