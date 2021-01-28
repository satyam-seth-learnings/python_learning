from threading import Thread
def disp():
    print('Child Thread')
t=Thread(target=disp)
t.start()
for i in range(5):
    print('Main Thread')