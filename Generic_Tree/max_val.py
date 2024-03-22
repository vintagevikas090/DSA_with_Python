'''Given a generic tree, find and return the node with maximum data. 
You need to return the node which is having maximum data.

Return null if tree is empty.'''

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

def printTreeDetailed(root):
    if root==None:
        return
    
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    
    for child in root.children:
        printTreeDetailed(child)


import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=TreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter num of children for",current_node.data)
        numChildren=int(input())
        for i in range(numChildren):
            print("Enter next child for",current_node.data)
            childData=int(input())
            child=TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root

def maxDataNode(root):
    if not root:
        return None
    maxNode = root # Assume that the root node has max Data
    for child in root.children:
        temp = maxDataNode(child)
        if temp.data > maxNode.data:
            maxNode = temp
    return maxNode

root=takeTreeInputLevelWise()
printTreeDetailed(root)
print('max = ', maxDataNode(root).data)