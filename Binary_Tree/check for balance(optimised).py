'''Check if the Binary Tree is Balanced or Not  (OPTIMISED CODE)
    (try to find height of left/right part and is_(left/right)_balance in one recursive call)'''

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

    
def get_Height_Check_Balance(root):
    if root is None:
        return 0, True
    leftHeight, is_left_Bal = get_Height_Check_Balance(root.left)
    rightHeight, is_right_Bal = get_Height_Check_Balance(root.right)
    
    valid_range = [-1, 0, 1]
    h = max(leftHeight, rightHeight) + 1
    
    if leftHeight - rightHeight not in valid_range:
        return h, False
    
    if is_left_Bal and is_right_Bal:
        return h, True
    else:
        return h, False
    
def is_Balanced(root):
    H, is_bal = get_Height_Check_Balance(root)
    return is_bal
    

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print()
print(is_Balanced(root))
