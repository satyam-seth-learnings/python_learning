from threading import Thread,current_thread
def disp():
    print('Disp Function')
mt=current_thread()
print(mt.getName())
print('MT:',mt.isDaemon())
t1=Thread(target=disp)
print('T1:',t1.isDaemon())
t1.start()