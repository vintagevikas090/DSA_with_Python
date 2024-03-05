'''Tree traversal'''

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

def preOrder(root):
    if root is None:
        print(-1, end = " ")
        return
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right)
    
def postOrder(root):
    if root is None:
        print(-1, end = " ")
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")
    
def InOrder(root):
    if root is None:
        print(-1, end = " ")
        return
    InOrder(root.left)
    print(root.data, end = " ")
    InOrder(root.right)
    
print('Enter the root value')
root = take_input_tree()
print_tree(root)
preOrder(root)
print()
postOrder(root)
print()
InOrder(root)
