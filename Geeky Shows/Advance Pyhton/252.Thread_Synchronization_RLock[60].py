from threading import *
class Flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=RLock()  #Or self.l=Lock()
        print(self.l)
    def reserve(self,need_seat):
        self.l.acquire()
        self.l.acquire()
        print(self.l)
        print('Available Seats:',self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()
        self.l.release()
        print(self.l)
f=Flight(2)
t1=Thread(target=f.reserve,args=(1,),name='Satyam')
t2=Thread(target=f.reserve,args=(1,),name='Ajay')
t3=Thread(target=f.reserve,args=(1,),name='Roy')
t1.start()
t2.start()
t3.start()