# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        if head.val == head.next.val:
            # temp = head
            # head = head.next
            # temp.next = None
            return self.deleteDuplicates(head.next)
        
        smalleroutput = self.deleteDuplicates(head.next)
        head.next = smalleroutput
        return head
        