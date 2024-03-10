'''Given the root of a binary tree, return the leftmost value in the last row of the tree.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return None
        
        queue = [root]
        leftmost = -1

        while queue:
            leftmost = queue.pop(0)

            if leftmost.right:
                queue.append(leftmost.right)
            # add left element after the right 
            if leftmost.left:
                queue.append(leftmost.left)

        return leftmost.val