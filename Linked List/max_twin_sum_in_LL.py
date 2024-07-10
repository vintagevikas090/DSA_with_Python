'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
'''
from typing import*
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''Method 1'''
        # data = []
        # temp = head
        # while temp is not None:
        #     data.append(temp.val)
        #     temp = temp.next
        
        # n = len(data)
        # max_s = float('-inf')
        # for i in range(n-1, -1, -1):
        #     if n-i-1 >= 0:
        #         s = data[i] + data[n-i-1]
        #         max_s = max(max_s, s)

        # return max_s


        '''Method 2'''
        # find mid
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # second_half head
        s_head = slow.next
        slow.next = None

        # rev second half
        prev = None
        curr = s_head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #rev_s_head = prev

        # iterate in both half(will be always equal in len)
        max_s = float('-inf')
        ptr1 = head
        ptr2 = prev

        while ptr1 and ptr2 is not None:
            s = ptr1.val + ptr2.val
            max_s = max(max_s, s)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return max_s

