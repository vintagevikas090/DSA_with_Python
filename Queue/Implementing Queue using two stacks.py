'''Implementing Queue using two stacks
    NOTE: One of the operation from enQueue or deQueue must be in O(1) Time Complexity '''

    
class Queue_using_stacks:
    def __init__(self):
        self.s1 = [] # To store Element
        self.s2 = []
        
    def emptyCheck(self):
        return len(self.s1) == 0
    
    def Qsize(self):
        return len(self.s1)
    
    def enQueue(self, data):
        self.s1.append(data)
        
    def deQueue(self):
        if self.emptyCheck():
            return -1
        
        if self.Qsize()==1:
            return self.s1.pop()
            
        else:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

            temp = self.s2.pop()

            while len(self.s2) != 0:
                self.s1.append(self.s2.pop())
            
            return temp
    
    def front_ele(self):
        if self.emptyCheck():
            return -1
        return self.s1[0]
    
q = Queue_using_stacks()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print('size = ' , q.Qsize())
print('front  =', q.front_ele())
print('Element taken Out = ', q.deQueue())
print('size = ', q.Qsize())
print('front = ', q.front_ele())
