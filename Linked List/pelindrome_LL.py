# Print reverse of the Linked List



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
    
def print_rev(head):
    li = []
    while head is not None:
        li.append(head.data)
        head = head.next
        
    for i in li[::-1]:
        print(i, end=" ")
        
def isPalindrome(head) :
    #Your code goes here
    li = []
    while head is not None:
        li.append(head.data)
        head = head.next

    if li == li[::-1]:
        print('true')
    else:
        print('false')
    
Head = take_input()
print_LL(Head)
print_rev(Head)
isPalindrome(Head)
