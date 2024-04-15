'''You have been given a singly linked list of integers along with two integers, 
'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, 
then delete the next 'N' nodes. Continue the same until the end of the linked list. Indexing starts from 1.

To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.'''



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

def skipMdeleteN(head, m, n):
    if (m == 1 and n == 0) or Length(head)<= m:
        return head
    if m == 0 or head is None:
        return None
    curr = head
    while curr is not None:
        i = 1 
        while i < m:
            if curr.next is not None:
                curr = curr.next
            i+=1
        if curr.next is not None:
            temp = curr.next
        j = 1
        while j < n:
            if temp.next is not None:
                temp = temp.next
            j += 1
        temp = temp.next
        curr.next = temp
        curr = temp
    return head

Head = take_input()
print_LL(Head)
skipMdeleteN(Head, 2, 3)
print_LL(Head)
