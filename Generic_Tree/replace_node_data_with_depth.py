'''Problem statement
You are given a generic tree. You have to replace each node with its depth value. 
You just have to update the data of each node, there is no need to return or print anything.'''

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

def replacewithDepthHelper(tree, depth):
    if not tree:
        return

    tree.data = depth

    for child in tree.children:
        replacewithDepthHelper(child, depth + 1)

def replacewithDepth(tree):
    replacewithDepthHelper(tree, 0)


root=takeTreeInputLevelWise()
replacewithDepth(root)
printTreeDetailed(root)
