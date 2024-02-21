'''For a given Binary Tree of integers, find and return the Number of all the nodes.'''

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

def Number_of_Nodes(root):
    if root == None:
        return 0
    leftCount = Number_of_Nodes(root.left)
    rightCount = Number_of_Nodes(root.right)
    return 1 + leftCount + rightCount

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print(Number_of_Nodes(root))
