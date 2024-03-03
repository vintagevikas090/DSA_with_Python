'''For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.

Return the output as an object of Pair class, which is already created.

Note:
All the node data will be unique and hence there will always exist a minimum and maximum node data.'''

class Pair :
    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum

# '''print Tree Levelwise'''

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

def isLeaf(node):
    return node.left is None and node.right is None

def print_Tree(root):
    if root is None:
        return 
    q = [root]
    while q:
        curr = q.pop(0)
        print(curr.data, end = ":")
        
        if curr.left is not None:
            leftData = curr.left.data
            print('L:', leftData ,end=",")
            q.append(curr.left)
        else:
            print('L:-1', end = ',')
            
        if curr.right is not None:
            rightData = curr.right.data
            print("R:", rightData, end = "")
            q.append(curr.right)
        else:
            print('R:-1', end = "")

        print()
        
def getMinAndMax(root):
    if root is None:
        return Pair(math.inf, -math.inf)

    min_value = root.data
    max_value = root.data

    if isLeaf(root):
        return Pair(min_value, max_value)

    left_pair = getMinAndMax(root.left)
    right_pair = getMinAndMax(root.right)

    min_value = min(min_value, left_pair.minimum, right_pair.minimum)
    max_value = max(max_value, left_pair.maximum, right_pair.maximum)

    return Pair(min_value, max_value)
        
root = level_wise_input()
print_Tree(root)
print(getMinAndMax(root).minimum, getMinAndMax(root).maximum)
