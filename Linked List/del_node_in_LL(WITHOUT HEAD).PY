'''
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.

'''

'''
How to delete the node when you dont have the head pointer?
The trick here is we can copy the data of the next node to the data field of the current node to be deleted.
 Then we can move one step forward. Now our next has become the current node and the current has become the previous node. 
 Now we can easily delete the current node by conventional deletion methods. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return 

        next_node = node.next
        next_data = next_node.val
        next_node.val = node.val
        node.val = next_data

        node.next = next_node.next

        return