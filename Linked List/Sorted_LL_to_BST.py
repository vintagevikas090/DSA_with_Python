'''Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def buildBST(self, l, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(l[mid])
            
        root.left = self.buildBST(l, left, mid - 1)
        root.right = self.buildBST(l, mid + 1, right)
            
        return root

    def sortedListToBST(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        return self.buildBST(values, 0, len(values) - 1)