from threading import Thread
def disp():
    for i in range(5):
        print('Child Thread')
t=Thread(target=disp)
t.start()
for i in range(5):
    print('Main Thread')