'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x: int):
        if head is None or head.next is None:
            return head

        small_head, large_head = None, None
        small_tail, large_tail = None, None

        temp = head
        while temp is not None:
            # data = ListNode(temp.val)
            next_node = temp.next
            temp.next = None
            if temp.val < x:
                if small_head is None:
                    small_head = temp
                    small_tail = temp
                else:
                    small_tail.next = temp
                    small_tail = small_tail.next
            else:
                if large_head is None:
                    large_head = temp
                    large_tail = temp
                else:
                    large_tail.next = temp
                    large_tail = large_tail.next

            temp = next_node

        # node_x = ListNode(x)
        if small_head is None and large_head is None:
            return None
        elif small_head is None and large_head is not None:
            return large_head
        elif large_head is None and small_head is not None:
            return small_head
        else:
            small_tail.next = large_head
            return small_head



