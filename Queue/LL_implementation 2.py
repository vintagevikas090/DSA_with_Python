'''Implementing Queue Using Linked List
   (without tail)'''

'''VARIATION 2 (insertion is done at the head of LL)'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def enQueue(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def deQueue(self):
        if self.isEmpty():
            return -1
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
            
        to_del = temp.next
        temp.next = None
        return to_del.data
    
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count+=1
            temp = temp.next
        return count
    
    def front_ele(self):
        if self.isEmpty():
            return -1
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.data
    
q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
# q.print_Queue()
print('size = ' , q.size())
print('front  =', q.front_ele())
print('Element taken Out = ', q.deQueue())
# q.print_Queue()
print('size = ', q.size())
print('front = ', q.front_ele())
