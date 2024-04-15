'''Reversing a linked list (without using additional space)'''


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

'''Iterative method'''
def Reverse_LL(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr is not None:
        next_of_curr = curr.next
        curr.next = prev 
        #prev.next = None
        prev = curr
        curr = next_of_curr

    head = prev
    return head

'''Recursive method 1'''
def reverseLinkedListRec(head) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    
    newHead = reverseLinkedListRec(head.next)
    temp = newHead
    while temp is not None:
        temp = temp.next
    temp.next = head
    head.next = None
    return newHead

'''Recursive method 1 (Optimised code)'''
def reverseLinkedListRec(head) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        temp = head
        head.next.next = head
        head = head.next
        temp.next = None
        return head
    newHead = reverseLinkedListRec(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return newHead



Head = take_input()
print_LL(Head)
Reverse_LL(Head)
print_LL(Head)
reverseLinkedListRec(Head)
print_LL(Head)
