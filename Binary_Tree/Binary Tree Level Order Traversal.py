'''
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = [root]
        next_queue = []
        level = []
        result = []
        
        while queue:
            # loop must be used becz we need access to all element of a level in each iteration
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        
        return result