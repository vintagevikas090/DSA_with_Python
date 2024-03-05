'''Print all Nodes Without Siblings '''

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

def No_Siblings(node, parent_of_node):
    if node is None:
        return False
    if parent_of_node.left == node:
        return parent_of_node.right == None
    else:
        return parent_of_node.left == None
    
def print_Nodes_without_siblings(root):
    if root is None:
        return 
    leftChild = root.left
    rightChild = root.right
    parent = root
    if leftChild  != None:
        if No_Siblings(leftChild, parent):
            print(leftChild.data, end = " ")
        print_Nodes_without_siblings(leftChild)
    else:
        if rightChild == None:
            return 
        else:
            if No_Siblings(rightChild, parent):
                print(rightChild.data, end= " ")
            print_Nodes_without_siblings(rightChild)
