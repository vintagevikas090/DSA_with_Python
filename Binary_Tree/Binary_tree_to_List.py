'''
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a 
formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c],
 place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        height = self.findHeight(root)
        num_rows = height + 1
        num_cols = 2**(height + 1) - 1

        res = [["" for c in range(num_cols)] for r in range(num_rows)]
        
        self.placeNodes(root, res, 0, num_cols//2, height)

        return res

    def findHeight(self, root, height=-1) -> int:
        if root is None:
            return height
        return max(self.findHeight(root.left, height+1), self.findHeight(root.right, height+1))

    def placeNodes(self, node, matrix, r, c, height) -> None:
        if node is None:
            return
        matrix[r][c] = str(node.val)
        self.placeNodes(node.left, matrix, r+1, c-(2**(height-r-1)), height)
        self.placeNodes(node.right, matrix, r+1, c+(2**(height-r-1)), height)