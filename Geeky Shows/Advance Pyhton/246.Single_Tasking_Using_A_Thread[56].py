from threading import Thread
from time import sleep
class MyExam:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print('Question 1 Solved')
        sleep(3)
    def q2(self):
        print('Question 2 Solved')
        sleep(3)
    def q3(self):
        print('Question 3 Solved')
        sleep(3)
mye=MyExam()
t=Thread(target=mye.solve_question)
t.start()