'''Given the root of a binary tree, flatten the tree into a linked list

The "linked list" should use the same TreeNode class where the right child pointer points 
to the next node in the list and the left child pointer is always null.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        stack = [root]
        prev = None
        #prev is required for the connection making with current

        while stack:
            current = stack.pop()

            if prev:
                prev.right = current
                prev.left = None

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            prev = current
        