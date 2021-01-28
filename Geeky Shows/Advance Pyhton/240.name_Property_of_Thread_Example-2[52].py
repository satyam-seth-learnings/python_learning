from threading import Thread
def disp():
    pass
t1=Thread(target=disp)
print('Default t1:',t1.getName())
t1.setName('Doc Thread')
print('New t1:',t1.getName())
t2=Thread(target=disp)
print('Default t2:',t2.name)
t2.name='Flying Thread'
print('New t2:',t2.name)
t3=Thread(target=disp,name='My Thread')
print(t3.name)