from threading import Thread,current_thread
from time import sleep
def teacher():
    for i in range(1,11):
        print('Teaching Session',i)
        sleep(1)
t1=Thread(target=teacher)
# t1.setDaemon(True)
t1.start()
sleep(6)
# t1.join()
print('Exam Finished',current_thread().name)