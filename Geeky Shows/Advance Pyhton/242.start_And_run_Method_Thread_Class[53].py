from threading import Thread
class Mythread(Thread):
    def run(self):
        print('Run Method')
t=Mythread()
print(t.name)
t.start()