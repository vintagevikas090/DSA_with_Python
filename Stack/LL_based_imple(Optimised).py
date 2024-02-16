'''Linked list implementation of stack'''

'''Using head pointer only (OPTIMISED CODE)

    Major operations should take constant time '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.count = 0

class stack:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def push(self, val):
        nn = Node(val)
        if self.isEmpty():
            self.head = nn
        # insert at head
        else:
            nn.next = self.head
            self.head = nn
            
        self.count = self.count+1
    
    def pop(self):
        if self.isEmpty():
            return -1
        temp = self.head
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            temp.next = None
        self.count = self.count - 1
        return temp.data
    
    def top(self):
        if self.isEmpty():
            return -1
        return self.head.data
    
    def size(self):
        return self.count
    
#         temp = self.head
#         cnt = 0
#         while temp is not None:
#             temp = temp.next
#             cnt += 1
#         return cnt
    
    def print_stack(self):
        temp = self.head
        print('Top to Bottom: ')
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
            
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.top())
print(s.pop())
print(s.top())
print(s.size())
s.print_stack()
