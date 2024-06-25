'''Check if the Binary Tree is Balanced or Not'''

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

def height(root):
    if root is None:
        return 0 
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return max(leftHeight, rightHeight) + 1

def is_BinaryTree_Balanced(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    
    valid_range = [-1, 0, 1]
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    if leftHeight - rightHeight not in valid_range:
        return False
    
    left_Bal = is_BinaryTree_Balanced(root.left)
    right_Bal = is_BinaryTree_Balanced(root.right)
    
    if left_Bal and right_Bal:
        return (height(root.left) - height(root.right)) in valid_range
    else:
        return False
    

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print()
print(is_BinaryTree_Balanced(root))
