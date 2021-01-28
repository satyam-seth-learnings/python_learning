from array import *
stu_roll=array('i',[101,102,103,104,105])
# Accessing Without Index
for el in stu_roll:
    print(el)
# Accessing With Index
n=len(stu_roll)
for i in range(n):
    print("Index",i,"=",stu_roll[i])