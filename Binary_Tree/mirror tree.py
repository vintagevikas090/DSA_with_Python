'''For a given Binary Tree of type integer, update it with its corresponding mirror image.'''

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

def mirrorBinaryTree(root) :
    # Your code goes here
    if root is None:
        return None
    if root.left == None and root.right == None:
        return root

    temp = root.right
    root.right = root.left
    root.left = temp 
    
    root.left = mirrorBinaryTree(root.left)
    root.right = mirrorBinaryTree(root.right)
    
    return root

print('Enter the root value')
root = take_input_tree()
print_tree(root)
nroot = mirrorBinaryTree(root)
print_tree(nroot)
