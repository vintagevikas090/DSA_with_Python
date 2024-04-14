# printing ith node of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def take_input():
    print('Enter the values you want to insert in Linked List(space Seperated): ')
    li = [int(i) for i in input().split()]
    head = None
    tail = None
    for ele in li:
        # assuming -1 as a terminater value
        if ele == -1:
            break
        nn = Node(ele)
        if head == None:
            head = nn
            tail = nn
        else:
            tail.next = nn
            tail = nn
    return head

def printIthNode(head, i):
    c=0
    while head:
        if c==i:
            print(head.data)
            return head.data
        
        head=head.next
        c=c+1
        
        
Head = take_input()
print(printIthNode(Head, 2))