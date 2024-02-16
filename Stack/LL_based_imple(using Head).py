'''Linked list implementation of stack'''

'''Using head pointer only 
    Time complexcity is O(n)'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def push(self, val):
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = newNode
        
    def pop(self):
        if self.isEmpty():
            return -1
        if self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            to_del = temp.next.data
            temp.next = None
            return to_del
        
    def top(self):
        if self.isEmpty():
            return -1
        if self.head.next is None:
            return self.head.data
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            return temp.data
    
    def size(self):
        cnt = 0
        while self.head is not None:
            cnt+=1
            self.head = self.head.next
        return cnt
    
    def print_stack(self):
        temp = self.head
        print('Bottom to top: ')
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.top())
print(s.pop())
print(s.top())
s.print_stack()
