from array import *
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1
stu_roll.insert(2,111)
print("Array After Insert")
n=len(stu_roll)
i=0
while (i<n):
    print(stu_roll[i])
    i+=1