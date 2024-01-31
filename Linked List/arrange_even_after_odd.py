'''For a given singly linked list of integers, 
arrange the nodes such that all the even number nodes are 
placed after the all odd number nodes. 
The relative order of the odd and even terms should remain unchanged.'''



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

def Even_after_Odd(head):
    if head is None or head.next is None:
        return head
    oddHead, evenHead, newOddHead, newEvenHead = None, None, None, None    

    while head is not None:
        if head.data % 2 != 0:
            if oddHead is not None:
                oddHead.next = head
                oddHead = oddHead.next
            else:
                oddHead = head   
                newOddHead = head 
        else:
            if evenHead is not None:
                evenHead.next = head
                evenHead = evenHead.next   
            else:
                evenHead = head    
                newEvenHead = head    
        head = head.next

    if newEvenHead is not None and oddHead is not None:
        oddHead.next = newEvenHead
        evenHead.next = None
        return newOddHead
        
    elif newOddHead is not None:
        return newOddHead

    return newEvenHead

Head = take_input()
print_LL(Head)
Even_after_Odd(Head)
print_LL(Head)
