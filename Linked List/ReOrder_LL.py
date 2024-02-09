'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mid(self, head):
        if head is None or head.next is None:
            return head
        slow, fast, prev = head, head, None
        while fast is not None and fast.next is not None:
            prev = slow 
            slow = slow.next 
            fast = fast.next.next
        # if prev is not None:
        #     prev.next = None
        return slow


    def reorderList(self, head) -> None:
        if head is None or head.next is None:
            return head
        mid = self.mid(head)
        # reverse the right part
        prev = None
        temp = mid
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        #prev will be the head of reversed part
        
        #merge two parts
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2

        return head