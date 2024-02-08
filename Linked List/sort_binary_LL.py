'''Sort a binary linked list'''
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None    

def sort_binary_LL(head):
    if head is None or head.next is None:
        return head
    oddHead, oddTail, evenHead, evenTail = None, None, None, None
    temp = head
    while temp is not None:
        next_node = temp.next
        temp.next = None
        if temp.val == 0:
            if evenHead is None:
                evenHead = temp
                evenTail = temp
            else:
                evenTail.next = temp
                evenTail = evenTail.next
        else:
            if oddHead is None:
                oddHead = temp
                oddTail = temp
            else:
                oddTail.next = temp
                oddTail = oddTail.next
        temp = next_node
        
    if evenHead is None and oddHead is None:
        return None
    elif evenHead is None:
        return oddHead
    elif oddHead is None:
        return evenHead
    else:
        evenTail.next = oddHead.next
        oddHead.next = None
        return evenHead
    
