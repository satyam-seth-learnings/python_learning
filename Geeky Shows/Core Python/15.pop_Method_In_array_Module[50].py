from array import *
stu_roll=array('i',[101,102,103,104,105])
for i in stu_roll:
    print(i)
stu_roll.pop()
print("After Pop")
for i in stu_roll:
    print(i)
stu_roll.pop(1)
print("After Pop")
for i in stu_roll:
    print(i)
r=stu_roll.pop(1)
print("After Pop")
for i in stu_roll:
    print(i)
print("Removed Element:",r)