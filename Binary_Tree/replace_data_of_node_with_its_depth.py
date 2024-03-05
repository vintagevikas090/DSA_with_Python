'''
For a given a Binary Tree of integers, replace each of its data with the depth of the tree.

Root is at depth 0, hence the root data is updated with 0. 
Replicate the same further going down the in the depth of the given tree.

The modified tree will be printed in the in-order fashion.'''

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
    

def take_input_tree():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    print('Enter the left child value for ', rootData)
    leftChild = take_input_tree()
    print('Enter the right child value for ', rootData)
    rightChild = take_input_tree()
    root.left = leftChild
    root.right = rightChild
    return root

def changeToDepthTree(root, count = 0) :
    #Your code goes here
    if root is None:
        return 
    root.data = count
    changeToDepthTree(root.left, count+1)
    changeToDepthTree(root.right, count+1)
    
print('Enter the root value')
root = take_input_tree()
print_tree(root)
changeToDepthTree(root)
print_tree(root)
