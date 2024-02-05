'''Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length


    def rotateRight(self, head, k: int):
        if head == None or head.next == None or k == 0:
            return head
        
        # if k is higher than length of linked list
        k = k % self.getLength(head)
        if k == 0:
            return head
        
        while k:
            temp = head
            while temp.next.next is not None:
                temp = temp.next
            
            tail = temp.next
            temp.next = None
            tail.next = head
            head = tail

            k -= 1

        return head
    
    '''better approach'''
    def rotateRight(self, head, k: int):
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        k = k % length
            
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        # we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        #( cut the linked list from here (after node 3) )
        newhead = tempNode.next
        newhead.next = None
        
        return newhead