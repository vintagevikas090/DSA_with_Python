'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, head1, head2):
        carry = 0
        sum_head, sum_tail = None, None
        while head1 is not None or head2 is not None or carry !=0 :
            if head1 == None:
                val1 = 0
            else:
                val1 = head1.val

            if head2== None:
                val2 = 0
            else:
                val2 = head2.val

            digit =( val1 + val2 + carry )%10
            carry = ( val1 + val2 + carry )//10

            data = ListNode(digit)

            if sum_head == None:
                sum_head = data
                sum_tail = data
            else:
                sum_tail.next = data
                sum_tail = sum_tail.next

            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next

        return sum_head