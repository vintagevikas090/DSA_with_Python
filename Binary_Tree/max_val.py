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

def Max_Data(root):
    if root == None:
        return -1
    leftMax = Max_Data(root.left)
    rightMax = Max_Data(root.right)
    MaxVal = max(leftMax, rightMax, root.data)
    return MaxVal

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print(Max_Data(root))