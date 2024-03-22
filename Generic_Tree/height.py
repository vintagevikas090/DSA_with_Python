'''find and return the height of given tree'''

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

def Height(root):
    if root is None:
        return 0
    if root.children is None:
        return 1
    max_child_h = 0
    for child in root.children:
        max_child_h = max(max_child_h, Height(child))

    return max_child_h+1

root=takeTreeInputLevelWise()
printTreeDetailed(root)
print('Height = ', Height(root))