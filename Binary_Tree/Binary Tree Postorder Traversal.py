'''Given the root of a binary tree, return the postorder traversal of its nodes' values.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        # result = []
        # if root is None:
        #     return result
        
        # result += self.postorderTraversal(root.left)
        # result += self.postorderTraversal(root.right)
        # result.append(root.val)

        # return result

        
        result = []
        stack = []

        if root is None:
            return result

        stack.append(root)

        while stack:
            current = stack.pop()

            # Insert at the beginning of the result list to simulate postorder traversal
            result.insert(0, current.val)

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

        return result