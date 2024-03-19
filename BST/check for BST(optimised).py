    '''Check for BST (OPTIMISED CODES)'''


# returns min, max, isBST 
def check_BST2(root):
    if root is None:
        return 100000, -100000, True
    
    leftMin, leftMax, isLeftBST = check_BST2(root.left)
    rightMin, rightMax, isRightBST = check_BST2(root.right)
    
    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    
    isBST = True
    if root.data < leftMax or root.data > rightMin:
        isBST = False
    
    if not isLeftBST or not isRightBST:
        isBST = False
        
    return minimum, maximum, isBST



def check_BST3(root, limit1 = -10000000, limit2 = 1000000):
    if root is None:
        return True
    if !(root.data>limit1 and root.data<limit2):
        return False
    isLeft_BST = check_BST3(root.left, limit1, root.data -1)
    isRight_BST = check_BST3(root.right, root.data, limit2)
    
    return isLeft_BST and isRight_BST