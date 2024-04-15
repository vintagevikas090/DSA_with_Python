'''Swap two nodes in linked list'''



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

def get_node_at_position(position, head):
        current = head
        for i in range(position):
            current = current.next
        return current

def swapNodes(head, i, j) :
    #Your code goes here
    if i == j:
        return head

    if i == 0:
        prev_of_i = None
        node_i = head
    else:
        prev_of_i = get_node_at_position(i - 1, head)
        node_i = prev_of_i.next

    prev_of_j = get_node_at_position(j - 1, head)
    node_j = prev_of_j.next

    # Swap the nodes
    if prev_of_i:
        prev_of_i.next = node_j
    else:
        head = node_j

    prev_of_j.next = node_i
    temp = node_i.next
    node_i.next = node_j.next
    node_j.next = temp

    return head

Head = take_input()
print_LL(Head)
swapNodes(Head, 3, 5)
print_LL(Head)
