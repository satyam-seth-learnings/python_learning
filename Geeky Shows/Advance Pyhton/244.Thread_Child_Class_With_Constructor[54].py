from threading import Thread
class Myrthread(Thread):
    def __init__(self,a):
        Thread.__init__(self)           #Or        RuntimeError: thread.__init__() not called
        print('Child Thread Constructor',a)
    def run(self):
        pass
t=Myrthread(10)
t.start()
print('Main Thread')