from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''


def is_complete_tree(node):
    if node is None:
        return True
    if node.right is not None and node.left is None:
        return False
    if node.right is None and node.left is not None and not (node.left.left is None and node.left.right is None):
        return False
    return True 


def is_heap(node):
    if node is None:
        return True
    if node.left and node.left.data > node.data:
        return False
    if node.right and node.right.data > node.data:
        return False
    return is_heap(node.left) and is_heap(node.right)

def isBinaryHeapTree(root):
    if root is None:
        return True
    return is_complete_tree(root) and is_heap(root)

