'''Given a node ele, return the path from that node to the root in BINARY TREE'''

def node_to_root_path(root, val):
    if root is None:
        return None
    if root.data == val:
        l = list()
        l.append(val)
        return l
    
    leftOutput = node_to_root_path(root.left, val)
    if leftOutput is not None:
        return leftOutput.append(root.data)
    
    rightOutput = node_to_root_path(root.right)    
    
    if rightOutput is None:
        return None
    else:
        return rightOutput.append(root.data)