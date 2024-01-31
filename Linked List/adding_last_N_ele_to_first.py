'''Adding Last N Elements to the front of the linked list'''



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

# def Append_Last_N_to_first(Head, N):
#     i = 1
#     curr = Head
#     while i < Length(curr)- N:
#         curr = curr.next
#         i+=1
#     newHead = curr.next
    
#     j = 1
#     temp = newHead
#     while j<N:
#         temp = temp.next
#         j+=1
#     temp.next = Head
#     curr.next = None
#     return newHead

def Append_Last_N_to_first(Head, n):
    if Head is None or n<=0:
        return Head
    first, last = Head, Head
    
    #make gap of 'n' between first and last
    for i in range(n-1):
        if last is None:
            return Head
        last = last.next
        
    prev_of_first = None
    
    # last ptr to the last position of the list
    while last.next is not None:
        prev_of_first = first
        first = first.next
        last = last.next
        
    newHead = first
    if prev_of_first is not None:
        prev_of_first.next = None
        
    last.next = Head
    #print(last.data)

    return newHead

Head = take_input()
print_LL(Head)
Append_Last_N_to_first(Head, 3)
print_LL(Head)
