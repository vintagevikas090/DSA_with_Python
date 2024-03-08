'''Given the root of a binary tree, return the postorder traversal of its nodes' values.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        result.append(root.val)
        
        result += self.preorderTraversal(root.left)

        result += self.preorderTraversal(root.right)

        return result