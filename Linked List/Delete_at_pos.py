# delete node at given position

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

def length(Head):
    cnt = 0
    while Head is not None:
        cnt+=1
        Head = Head.next
    return cnt

''' Assuming pos of first element to be 0  '''
def deleteNode(head, pos) :
    if pos<0 or pos>length(head) or head is None:
        return head
    if pos ==  0 or length(head)==1:
        to_del = head
        head = head.next 
        to_del.next = None
        del to_del
    else:
        i = 1
        temp = head
        while i<pos:
            temp = temp.next
            i+=1
        to_del = temp.next
        temp.next = to_del.next
        to_del.next = None
        del to_del
    return head
   
    
def print_LL(head):
    print('Linked list is:')
    while(head != None):
        print(head.data, end= "")
        print('->', end="")
        head = head.next
    print('None')
    
    
Head = take_input()
print_LL(Head)
deleteNode(Head, 3)
print_LL(Head)