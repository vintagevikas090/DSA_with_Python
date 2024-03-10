'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root
'''
'''
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str):
        stack = []
        i = 0
        
        while i < len(traversal):
            depth = 0
            val = ""
            # for Number of dash or depth of node
            while i < len(traversal) and traversal[i] == "-":
                depth += 1
                i += 1
            
            # to get value for a node
            while i < len(traversal) and traversal[i] != "-":
                val += traversal[i]
                i += 1
            
            node = TreeNode(int(val))
            
            # handle childs for "node"
            
            if depth == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]