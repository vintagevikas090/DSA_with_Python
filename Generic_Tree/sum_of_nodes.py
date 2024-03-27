class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

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

def printTreeDetailed(root):
    if root==None:
        return
    
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    
    for child in root.children:
        printTreeDetailed(child)
        
def sumOfAllNodes(root) :
    if root is None:
        return 0
    sum = root.data
    for child in root.children:
        sum += sumOfAllNodes(child)

    return sum

root = takeTreeInputLevelWise()
printTreeDetailed(root)
print()
print(sumOfAllNodes(root))