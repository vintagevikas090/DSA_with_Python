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


# sol 2
class Solution:
    
    def helper(self, root) -> int:
        if not root:
            return (0, -1)
        
        if root.left is None and root.right is None:
            return (1, root.val)
        
        lh, v1 = self.helper(root.left)
        rh, v2 = self.helper(root.right)
        
        h = max(lh, rh) + 1
        if lh>=rh:
            return (h, v1)
        else:
            return (h, v2)
    
    def findBottomLeftValue(self, root) -> int:
        return self.helper(root)[1]
