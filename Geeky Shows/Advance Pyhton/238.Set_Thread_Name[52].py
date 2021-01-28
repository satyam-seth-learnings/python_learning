from threading import Thread,current_thread
def disp():
    print('Default Child Thread Name:',current_thread().getName())
    current_thread().setName('Doc Thread')
    print('New Child Thread Name:',current_thread().getName())
t=Thread(target=disp)
t.start()
print('Default Main Thread Object Name:',current_thread().getName())
current_thread().setName('Satyam Thread')
print('New Main Thread Name:',current_thread().getName())