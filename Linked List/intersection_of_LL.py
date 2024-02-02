'''Intersection point between two linked List'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        ptr1 = headA
        ptr2 = headB

        while ptr1 != ptr2:
            if ptr1 is not None:
                ptr1= ptr1.next
            else:
                ptr1 = headB

            if ptr2 is not None:
                ptr2 = ptr2.next
            else:
                ptr2 = headA

        return ptr1