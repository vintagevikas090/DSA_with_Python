'''Merging 2 sorted Linked List'''



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

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data<=head2.data:
        newHead = head1
        ptr1 = head1.next
        ptr2 = head2
    else:
        newHead = head2
        ptr1 = head1
        ptr2 = head2.next
        
    temp = newHead
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data<=ptr2.data:
            temp.next = ptr1
            ptr1 = ptr1.next
        else:
            temp.next = ptr2
            ptr2 = ptr2.next
        temp = temp.next
        
    if ptr1 is not None:
        temp.next = ptr1
    else:
        temp.next = ptr2
        
    return newHead

Head1 = take_input()
Head2 = take_input()

a = merge(Head1, Head2)
print_LL(a)
