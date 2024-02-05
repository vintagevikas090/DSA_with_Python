'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        newHead = self.reverseLL(head.next)
        tail = head.next
        tail.next = head
        head.next = None 
        return newHead

    def getLength(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def reverseKGroup(self, head, k: int):
        if head is None or head.next is None or self.getLength(head)<k:
            return head
        if k <= 1: 
            return head
        i = 1
        temp = head
        oldHead = head
        while i<k:
            if temp.next is not None:
                temp = temp.next
            i+=1
        smallHead = temp.next
        temp.next = None
        newSmallHead = self.reverseKGroup(smallHead, k)
        newHead = self.reverseLL(head)
        oldHead.next = newSmallHead
        return newHead