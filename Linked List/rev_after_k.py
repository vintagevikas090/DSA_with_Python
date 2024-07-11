'''Given a singly linked list of integers, 
  reverse the nodes of the linked list 'k' at a time and return its modified list.

 'k' is a positive integer and is less than or equal to the length of the linked list. 
 If the number of nodes is not a multiple of 'k,' then left-out nodes,
 in the end, should be reversed as well.

Example :
Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4'''




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

def reverseLL(head):
    if head is None or head.next is None:
        return head
    newHead = reverseLL(head.next)
    tail = head.next
    tail.next = head
    head.next = None 
    return newHead

def kReverse(head, k) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    if k <= 1: 
        return head
    i = 1
    temp = head
    oldHead = head
    while i<k:
        if temp.next is not None:
            temp = temp.next
        i+=1
    smallHead = temp.next
    temp.next = None
    newSmallHead = kReverse(smallHead, k)
    newHead = reverseLL(head)
    oldHead.next = newSmallHead
    return newHead

Head = take_input()
print_LL(Head)
Head = kReverse(Head,2)
print_LL(Head)
