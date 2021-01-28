from threading import Thread
class Mythread:
    def disp(self,a,b):
        print(a,b)
myt=Mythread()
t=Thread(target=myt.disp,args=(10,20))
t.start()