# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        newHead = self.reverseList(head.next)
        tail = head.next
        head.next = None
        tail.next = head
        return newHead
    

    '''method 1 (better)'''
    def isPalindrome(self, head) -> bool:
        if head is None or head.next is None:
            return True
        
        slow, fast = head, head 

        # Finding Midpoint 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        rev_head = self.reverseList(mid)

        ptr1 = head
        ptr2 = rev_head

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True
    
    def isPalindrome2(self, head) -> bool:
        if head is None or head.next is None:
            return True
        rev_head = self.reverseList(head)

        ptr1 = head
        ptr2 = rev_head
        
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True