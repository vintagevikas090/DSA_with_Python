'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
'''

from typing import*
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #@ find all possible paths from LEAF to ROOT
    def find_paths(self, root, res, s = ''):
        if root is None:
            return res
        s += chr(root.val + 97)
        if root.left is None and root.right == None:
            res.append(s[::-1]) 
            return res
        self.find_paths(root.left, res, s)
        self.find_paths(root.right, res, s)
        return res

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        output = self.find_paths(root, [])
        output.sort()
        return output[0]
