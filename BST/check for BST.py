    '''Check if a Binary tree is BST or Not'''
def isLeaf(node):
    return node.left is None and node.right is None

def Minima_of_BST(root):
    if root is None:
        return 1000000
    leftMin = Minima_of_BST(root.left)
    rightMin = Minima_of_BST(root.right)
    return min(leftMin, rightMin, root.data)

def Maxima_of_BST(root):
    if root is None:
        return -1000000
    leftMax = Maxima_of_BST(root.left)
    rightMax = Maxima_of_BST(root.right)
    return max(leftMax, rightMax, root.data)

def check_BST(root):
    if root is None or isLeaf(root):
        return True
    
    Min_left = Minima_of_BST(root.left)
    Max_right = Maxima_of_BST(root.right)
    
    if not (root.data < Max_right or root.data > Min_left):
        return False
    
    leftCheck = check_BST(root.left)
    rightCheck = check_BST(root.right)
    
    if leftCheck and rightCheck:
        return True
    else:
        return False