'''Remove all the leaf Nodes from the tree'''

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

def isLeaf(node):
    return node.left == None and node.right == None

def remove_Leaf(root):
    if root is None:
        return root
    if isLeaf(root):
        return None
    root.left = remove_Leaf(root.left)
    root.right = remove_Leaf(root.right)
    return root
        

print('Enter the root value')
root = take_input_tree()
print_tree(root)
nroot = remove_Leaf(root)
print_tree(nroot)
