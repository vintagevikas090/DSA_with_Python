'''Implementing Stack using two Queues'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def Empty(self):
        return self.head == None
    
    def enQueue(self, val):
        newNode = Node(val)
        if self.Empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
        self.count += 1
        
    def deQueue(self):
        if self.Empty():
            return -1
        temp = self.head
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            
        self.count-=1
        return temp.data
    
    def size(self):
        return self.count
    
    def front_ele(self):
        if self.Empty():
            return -1
        return self.head.data
    
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def getSize(self):
        return self.q1.size()
    
    def isEmpty(self):
        return self.q1.Empty()
    
    def push(self, data):
        self.q1.enQueue(data)
        
    def pop(self):
        if self.isEmpty():
            return -1
        if self.getSize()==1:
            return self.q1.deQueue()
        while self.q1.size()!= 1:
            self.q2.enQueue(self.q1.deQueue())
            
        temp = self.q1.deQueue()
        
        while self.q2.size()!= 0:
            self.q1.enQueue(self.q2.deQueue())
        return temp
    
    def top(self):
        if self.isEmpty():
            return -1
        if self.getSize()==1:
            return self.q1.front_ele()
        while self.q1.size()!= 1:
            self.q2.enQueue(self.q1.deQueue())
            
        temp = self.q1.front_ele()
        
        while self.q2.size()!= 0:
            self.q1.enQueue(self.q2.deQueue())
        return temp
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.pop())
print(s.top())
