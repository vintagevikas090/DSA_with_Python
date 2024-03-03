'''Search for a node with value X in a binary Tree'''

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

def Search_Node(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    p = Search_Node(root.left, x)
    if not p:
        return Search_Node(root.right, x)
    else:
        return p

print('Enter the root value')
root = take_input_tree()
print_tree(root)
val = int(input('Enter the value you want to search: '))
print(Search_Node(root, val))
