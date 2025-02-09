# Queue and Stack tasks
from collections import deque

class trainReservation:
    
    def __init__(self,lnkLt,stac,queu):
        self.lnkLt = lnkLt
        self.stac = stac
        self.queu = queu

    def BookTicket(self,num):
        if num <= 10:
            self.lnkLt.append(num)
            self.queu.append(num)
        else:
            self.stac.append(num)
    def CancelBooking(self, num):
        for i in range(len(self.queu)):
            if(self.queu.pop()==num):
                print('ticket is poped')
            else:
                for i in range(len(self.stac)):
                    if(self.stac.pop()==num):
                        print('ticket is poped')
    def DisplayPassengrs(self):
        print('Booked Passengrs: ')
        for i in range(len(self.queu)): 
            print(self.queu.pop())
        print('Waiting Passengrs: ')
        for i in range(len(self.stac)): 
            print(self.stac.popleft())
        
TR = trainReservation([],deque([]),deque([]))

TR.BookTicket(4);
TR.BookTicket(5);
TR.CancelBooking(4)
TR.DisplayPassengrs()

# task2
class Schedulling:
    def __init__(self,LinkList,stack,queue):
        self.LinkList = LinkList;
        self.stack = stack;
        self.queue = queue;
    def AddTask(self, num,prior):
        self.LinkList = num;
        if(prior==1):
            self.stack.append(num)
        else:
            self.queue.append(num)
    def ExecuteTask(self):
        for i in range(len(self.stack)):
            print('More Priority task: '+str(self.stack.popleft()))
        for i in range(len(self.queue)):
            print('Less Priority task: '+str(self.queue.pop()))
    def RemoveTask(self, num):
        for i in range(len(self.stack)):
            if(self.stack.pop()==num):
                print('Task is removed')
            else:
                for i in range(len(self.queue)):
                    if(self.queue.pop()==num):
                        print('Task is removed')
                        
SH = Schedulling([],deque([]),deque([]))
SH.AddTask(1,1)
SH.ExecuteTask()