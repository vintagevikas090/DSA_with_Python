'''# Recursive Insertion in Linked List'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def build_LL(values):
    head = None
    tail = None
    for i in values:
        if i == -1:
            break
        newNode = Node(i)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def take_input():
    print('Enter the value you want to insert in linked list(space seperated): ')
    li = [int(i) for i in input().split()]
    return build_LL(li)

def print_LL(head):
    print('Linked List is as Following: ')
    while head is not None:
        print(head.data, end="")
        print('--> ', end= "")
        head = head.next
    print('None')
    
def Length(Head):
    cnt = 0
    while Head is not None:
        cnt+=1
        Head = Head.next
    return cnt

def Recursive_insertion(head, pos, val):
    if pos<0 or pos>Length(head):
        return -1
    newNode = Node(val)
    if head is None:
        head = newNode
    elif pos == 0:
        newNode.next = head
        head = newNode
    else:
        tempHead = Recursive_insertion(head.next, pos-1, val)
        head.next = tempHead
    return head

Head = take_input()
print_LL(Head)
Recursive_insertion(Head, 2, 22)
print_LL(Head)
