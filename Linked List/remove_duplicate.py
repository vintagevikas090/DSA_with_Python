'''Remove Duplicates from the linked list'''


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

def Remove_Duplicates(head):
    if head is None or head.next is None:
        return head
    if head.data == head.next.data:
        temp = head.next
        head.next = temp.next
        temp.next = None
        return Remove_Duplicates(head)
    else:
        return Remove_Duplicates(head.next)

Head = take_input()
print_LL(Head)
Remove_Duplicates(Head)
print_LL(Head)
