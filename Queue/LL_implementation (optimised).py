'''Implementing Queue Using Linked List (Optimised Code (using Tail))

    All main function are having Time Complexity of O(1) '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def isEmpty(self):
        return self.head == None
    
    def enQueue(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
        self.count += 1
        
    def deQueue(self):
        if self.isEmpty():
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
        if self.isEmpty():
            return -1
        return self.head.data
    
    def print_Queue(self):
        temp = self.head
        print('Queue is as following: ')
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        print()
    
q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.print_Queue()
print('size = ' , q.size())
print('front  =', q.front_ele())
print('Element taken Out = ', q.deQueue())
q.print_Queue()
print('size = ', q.size())
print('front = ', q.front_ele())
