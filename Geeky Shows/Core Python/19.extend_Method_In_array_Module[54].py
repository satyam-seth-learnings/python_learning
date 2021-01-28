from array import *
stu_roll=array('i',[101,102,103])
arr=array('i',[104,105])
for i in stu_roll:
    print(i)
stu_roll.extend(arr)
print("Array After Extend")
for i in stu_roll:
    print(i)