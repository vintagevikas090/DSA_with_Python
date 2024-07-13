'''reverse linked list in the given range'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head

        pre_left = None
        current = head

        for _ in range(left - 1):
            pre_left = current
            current = current.next

        smallhead = current
        pre_left.next = None

        # Reverse the sublist
        prev = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        smallhead.next = current
        pre_left.next = prev

        return head