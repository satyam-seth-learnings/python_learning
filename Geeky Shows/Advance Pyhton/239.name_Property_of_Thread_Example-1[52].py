from threading import Thread,current_thread
def disp():
    print('Default Child Name:',current_thread().name)
    current_thread().name='Flying Thread'
    print('New Child Name:',current_thread().name)
t=Thread(target=disp)
t.start()
print('Default Main Name:',current_thread().name)
current_thread().name='Geek Thread'
print('New Main Name:',current_thread().name)