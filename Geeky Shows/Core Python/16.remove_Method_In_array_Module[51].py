from array import *
stu_roll=array('i',[101,102,103,104,105])
for i in stu_roll:
    print(i)
stu_roll.remove(103)
print("After remove")
for i in stu_roll:
    print(i)