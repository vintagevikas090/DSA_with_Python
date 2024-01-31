'''Finding Index of a particular node in linked list'''



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

def index_of_Num(head, n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    smallOutput = index_of_Num(head.next, n)
    if smallOutput == -1:
        return -1
    else:
        return smallOutput + 1
    

Head = take_input()
print_LL(Head)
num = int(input())
print(index_of_Num(Head, num))
