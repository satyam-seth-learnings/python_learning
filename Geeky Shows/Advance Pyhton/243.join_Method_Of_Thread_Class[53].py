from threading import Thread
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')
t=Mythread()
t.start()
t.join()
for i in range(5):
    print('Main Thread')