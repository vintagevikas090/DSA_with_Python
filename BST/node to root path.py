'''Given a node ele, return the path from that node to the root in BST'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPathBST(root, val):
    if root is None:
        return []
    if root.data == val:
        l = list()
        l.append(val)
        return l
    if val < root.data:
        leftOutput = findPathBST(root.left, val)
        if leftOutput:
            leftOutput.append(root.data)
            return leftOutput
        else:
            return []
    else:
        rightOutput = findPathBST(root.right, val)
        if rightOutput:
            rightOutput.append(root.data)
            return rightOutput
        else:
            return []
