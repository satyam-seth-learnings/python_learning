import os
print(os.getcwd())
os.mkdir('mydir')
os.mkdir('mydir/mychilddir')
os.makedirs('parentdir/childdir/gradchilddir')
os.chdir('change folder')
print(os.getcwd())
os.rename('old name','new name')
os.rmdir('remove')
os.rmdir('remove parent/remove child')
os.removedirs('r1/r2/r3')
print('Current Directory:')
w1=os.walk('.')
for i in w1:
    print(i)
print('walk folder topdwon=True:')
w2=os.walk('walk folder',topdown=True)
for i in w2:
    print(i)
print('walk folder topdwon=False:')
w3=os.walk('walk folder',topdown=False)
for i in w3:
    print(i)