'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

ASSUME INDEXING STARTS FROM 1

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        oddHead, oddTail, evenHead, evenTail = None, None, None, None
        temp = head
        i = 1
        while temp is not None:
            next_node = temp.next
            temp.next = None
            if i % 2 == 0:
                if evenHead is None:
                    evenHead = temp
                    evenTail = temp
                else:
                    evenTail.next = temp
                    evenTail = evenTail.next
            else:
                if oddHead is None:
                    oddHead = temp
                    oddTail = temp
                else:
                    oddTail.next = temp
                    oddTail = oddTail.next
            temp = next_node
            i+=1
            
        if evenHead is None and oddHead is None:
            return None
        elif evenHead is None:
            return oddHead
        elif oddHead is None:
            return evenHead
        else:
            oddTail.next = evenHead
            evenTail.next = None
            return oddHead