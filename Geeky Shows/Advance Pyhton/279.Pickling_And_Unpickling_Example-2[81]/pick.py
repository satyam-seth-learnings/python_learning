# pick.py
# Storing Object In The File
import pickle,stu
n=int(input('Enter Number Of Students:'))
with open('student.dat','wb') as f:
    for i in range(n):
        name=input('Enter Student Name:')
        roll=input('Enter Student Roll:')
        address=input('Enter Student Address:')
        stu1=stu.Student(name,roll,address)
        pickle.dump(stu1,f)
    print('Pickling Done!!..')