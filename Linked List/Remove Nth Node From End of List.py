'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head is None or head.next is None and n == 1:
            return None

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Edge case: removing the head node
        if length == n:
            return head.next

        # Find the node before the one to be removed
        target_index = length - n
        current = head
        for _ in range(target_index - 1):
            current = current.next

        # Remove the nth node from the end
        current.next = current.next.next

        return head