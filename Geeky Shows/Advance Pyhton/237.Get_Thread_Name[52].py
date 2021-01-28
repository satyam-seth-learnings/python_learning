from threading import Thread,current_thread
def disp():
    print('Child Thread Object:',current_thread())
    print('Child Thread Object Name:',current_thread().getName())
t1=Thread(target=disp)
t2=Thread(target=disp)
t1.start()
t2.start()
print('Main Thread Object:',current_thread())
print('Main Thread Object Name:',current_thread().getName())