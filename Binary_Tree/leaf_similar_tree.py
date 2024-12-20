'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 
Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
'''
from typing import*
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_leaf(self, node):
        return node.left is None and node.right == None
    def get_leaf(self, root, leaves=[]):
        if root is None:
            return leaves
        if self.is_leaf(root):
            leaves.append(root.val)
            return leaves
        self.get_leaf(root.left, leaves)
        self.get_leaf(root.right, leaves)
        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        l1 = self.get_leaf(root1, [])
        l2 = self.get_leaf(root2, [])
        return l1 == l2


