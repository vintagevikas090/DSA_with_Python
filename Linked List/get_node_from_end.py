'''
get the node value at some position from tail

'''

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def revLL(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def getNode(llist, pos):
    # Write your code here
    head = revLL(llist)
    temp = head
    index = 0
    while temp is not None:
        if index == pos:
            return temp.data
        temp = temp.next
        index += 1
    
