'''For a given Binary Tree of integers, find and return the sum of all the nodes data.'''

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

def Sum_of_Nodes(root):
    if root == None:
        return 0
    leftSum = Sum_of_Nodes(root.left)
    rightSum = Sum_of_Nodes(root.right)
    return leftSum + rightSum + root.data

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print(Sum_of_Nodes(root))
