# index of an element in linked list

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

def find_Node(head, num):
    if head is None:
        return -1
    else:
        index = 0
        temp = head
        while temp is not None:
            if temp.data != num:
                index+=1
                temp = temp.next
            else:
                return index
    return -1

Head = take_input()
print(find_Node(Head, 56))