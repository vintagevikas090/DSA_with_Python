'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

from typing import*

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        newhead = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return newhead