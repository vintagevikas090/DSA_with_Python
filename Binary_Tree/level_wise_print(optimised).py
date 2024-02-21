'''For a given a Binary Tree of type integer, print it in a level order fashion where each level
will be printed on a new line. Elements on every level will be printed in a linear fashion and 
a single space will separate them.'''


import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
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

# Method 1

def print_given_level(root, level):
    if root is None:
        print(-1, end = " ")
        return
    if level == 0:
        print(root.data, end = " ")
        return 
    else:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)
        
def Height(root):
    if root is None:
        return 0
    leftHeight = Height(root.left)
    rightHeight = Height(root.right)
    h = max(leftHeight, rightHeight) + 1
    return h

def print_levelWise(root):
    if root is None:
        return
    for i in range(Height(root)):
        print_given_level(root, i)
        print()
        
'''Optimised code'''
def printLevelWise(root):
    #Your code goes here
    if root == None:
        return
    q = [root]

    while len(q) != 0:
        current_len = len(q)
        for i in range(current_len):
            curr = q.pop(0)
            print(curr.data, end = " ")

            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

        print()
        
root = level_wise_input()
# print_levelWise(root)
printLevelWise(root)
