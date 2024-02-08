'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        temp = head.next
        next_node = temp.next
        temp.next = None

        #rev two nodes
        head.next = None
        temp.next = head
        head = temp
        # head.next.next = next_node
        smallerOutput = self.swapPairs(next_node)
        head.next.next = smallerOutput
        return head
