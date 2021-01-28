from threading import Thread
def disp1():
    print('Thread Running')
t1=Thread(target=disp1)
t1.start()
def disp2(a):
    print('Thread Running',a)
t2=Thread(target=disp2,args=(10,))
t2.start()
def disp3(a,b):
    print('Thread Running',a,b)
t3=Thread(target=disp3,args=(20,30))
t3.start()
for i in range(5):
    t=Thread(target=disp1)
    t.start()