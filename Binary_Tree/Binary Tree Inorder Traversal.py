'''Given the root of a binary tree, return the inorder traversal of its nodes' values.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)
            return result

        left_part = self.inorderTraversal(root.left)
        right_part = self.inorderTraversal(root.right)

        result = left_part + [root.val] + right_part

        return result
    
class Solution:
    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result
        
        result += self.inorderTraversal(root.left)

        result.append(root.value)

        result += self.inorderTraversal(root.right)

        return result
    

