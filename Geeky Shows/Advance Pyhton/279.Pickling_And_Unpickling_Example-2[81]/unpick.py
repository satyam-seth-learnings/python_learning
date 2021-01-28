# unpick.py
# Reading Object From The File
import pickle,stu
with open('student.dat','rb') as f:
    while True:
        try:
            obj=pickle.load(f)
            obj.disp()
        except EOFError:
            print('Unpickling Done!!..')
            break