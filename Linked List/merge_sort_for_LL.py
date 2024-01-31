'''Merge sort for linked list'''



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

def Mid_element_of_LL(head):
    if head is None:
        return head

    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


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

def Merge_sort(head):
    '''finding mid of the list'''
    if head is None:
        return head
    if head.next is None:
        return head

    mid = Mid_element_of_LL(head)
    
    '''make to part of the list'''
    h1 = head
    h2 = mid.next
    mid.next = None

    h1 = Merge_sort(h1)
    h2 = Merge_sort(h2)
    return merge(h1, h2)

Head = take_input()
print_LL(Head)
Merge_sort(Head)
print_LL(Head)
