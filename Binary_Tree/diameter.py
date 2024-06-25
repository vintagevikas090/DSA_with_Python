'''Find Diameter of the tree
    Diameter - distance between the farthest nodes in tree Or Number of edges between two farthest nodes'''

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

def Diameter(root):
    if root is None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    d1 = leftHeight + rightHeight
    d2 = Diameter(root.left)
    d3 = Diameter(root.right)
    return max(d1, d2, d3)

'''Optimised Code'''
# returns height, diameter
def Height_and_diameter(root):
    if root is None:
        return 0, 0
    leftHeight, dia_of_left  = Height_and_diameter(root.left)
    rightHeight, dia_of_right = Height_and_diameter(root.right)
    h = max(leftHeight, rightHeight)+1
    d1 = leftHeight + rightHeight
    d2 = dia_of_left
    d3 = dia_of_right
    return h, max(d1, d2,d3)

def getDiameter(root):
    h, dia = Height_and_diameter(root)
    return dia

print('Enter the root value')
root = take_input_tree()
print_tree(root)
print()
print(Diameter(root))
print(getDiameter(root))
