'''Deleting a node from BST'''

def isLeaf(node):
    return node.left == None and node.right == None

def minVal(root):
    if root is None:
        return 100000
    if root.left is None:
        return root.data
    return minVal(root.left)

def delete_node(root, val):
    if root is None:
        return None, False
    
    if val < root.data:
        left_root, is_left_del = delete_node(root.left, val)
        root.left = left_root
        return root, is_left_del
    
    elif val > root.data:
        right_root, is_right_del = delete_node(root.right, val)
        root.right = is_right_del
        return root, is_right_del
    
    else:
        # 0 child node
        if isLeaf(root):
            return None, True
        # 1 child node
        elif root.right is None and root.left is not None:
            return root.left, True
        elif root.right is not None and root.left is None:
            return root.right, True
        # 2 child nodes
        else:
            temp = minVal(root.right)
            root.data = temp
            new_right, is_del = delete_node(root.right, temp)
            root.right =  new_right
            return root, is_del
