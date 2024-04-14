'''Insertion Sort'''

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

def insertion_sort(head):
    if head is None or head.next is None:
        return head
    
    sorted_head = None
    
    while head is not None:
        current = head
        head = head.next
        
        if sorted_head is None or sorted_head.data > current.data:
            current.next = sorted_head
            sorted_head = current

        else:
            temp = sorted_head
            while temp.next is not None and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current

    return sorted_head

head = take_input()
print_LL(head)
head = insertion_sort(head)
print_LL(head)