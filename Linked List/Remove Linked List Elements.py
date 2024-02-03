'''Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        if head is None:
            return head
        if head.val == val and head.next is None:
            return None
        if head.val != val:
            smallerOutput = self.removeElements(head.next, val)
            head.next = smallerOutput
            return head
        else:
            # temp = head
            # head = head.next
            # temp.next = None
            return self.removeElements(head.next, val)