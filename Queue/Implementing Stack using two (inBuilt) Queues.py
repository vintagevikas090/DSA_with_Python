'''Implementing Stack using two Queues (Using in-Built Queue)'''

import queue

class stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
    
    def getSize(self):
        return self.q1.qsize()
    
    def isEmpty(self):
        return self.q1.empty()
    
    def push(self, data):
        self.q1.put(data)
        
    def pop(self):
        if self.isEmpty():
            return -1
        if self.getSize()==1:
            return self.q1.get()
        while self.q1.qsize()!= 1:
            self.q2.put(self.q1.get())
            
        temp = self.q1.get()
        
        while self.q2.qsize()!= 0:
            self.q1.put(self.q2.get())
        return temp
    
    def top(self):
        if self.isEmpty():
            return -1
        if self.getSize()==1:
            temp = self.q1.get()
            self.q1.put(temp)
            return temp
        while self.q1.qsize()!= 1:
            self.q2.put(self.q1.get())
            
        temp = self.q1.get()
        self.q2.put(temp)
        
        while self.q2.qsize()!= 0:
            self.q1.put(self.q2.get())
        return temp
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.pop())
print(s.top())
