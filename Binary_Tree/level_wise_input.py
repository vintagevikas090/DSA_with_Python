'''Taking Input Levelwise
    HINT: element that comes first, You need to ask for the children of that node first'''

import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def print_tree(root):
    if root == None:
        return
    print('node =', root.data, end = ":--> ")
    if root.left is not None:
        print('left = ', root.left.data, end = ", ")
    if root.right is not None:
        print('right = ', root.right.data, end = " ")
    print()
    print_tree(root.left)
    print_tree(root.right)
    
def level_wise_input():
    q = queue.Queue()
    rootData = int(input('Enter Root Data: '))
    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)
    while not q.empty():
        front = q.get()
        print('Enter the Left Child Data for', front.data)
        leftData = int(input())
        if leftData != -1:
            leftChild = Node(leftData)
            front.left = leftChild
            q.put(leftChild)
        
        print('Enter the Right Child Data for', front.data)
        rightData = int(input())
        if rightData != -1:
            rightChild = Node(rightData)
            front.right = rightChild
            q.put(rightChild)
    return root
        
        
root = level_wise_input()
print_tree(root)
