from threading import Thread,current_thread
class Flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
    def reserve(self,need_seat):
        print('Available Seats:',self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print('Sorry! All seats has alloted')
f=Flight(1)
t1=Thread(target=f.reserve,args=(1,),name='Satyam')
t2=Thread(target=f.reserve,args=(1,),name='Ajay')
t1.start()
t2.start()