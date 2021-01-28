from array import *
stu_roll=array('i',[])
n=int(input("Enter Number Of The Elements: "))
for i in range(n):
    stu_roll.append(int(input("Enter The Element: ")))
for i in range(len(stu_roll)):
    print(stu_roll[i])