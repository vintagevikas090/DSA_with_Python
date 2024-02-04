'''# Recursive Deletion in Linked List '''



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
    
def delete_Recursive(Head, pos):
    if Head is None or pos<0 or pos>Length(Head):
        return -1
    if Length(Head) == 1:
        del Head
        return None
    if Length(Head)>1 and pos == 0:
        temp = Head
        Head = temp.next
        temp.next = None
        del temp
    else:
        tempHead = delete_Recursive(Head.next, pos-1)
        Head.next = tempHead
    return Head
    
    
Head = take_input()
print_LL(Head)
print(Length(Head))
delete_Recursive(Head, 3)
print_LL(Head)
