'''Given a generic tree, find and return the node for which sum of its data and data of all its child nodes is maximum.
In the sum, data of the node and data of its immediate child nodes has to be taken.'''

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

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

def maxSumNode(root):
    if root is None:
        return None, 0

    maxNode, maxVal =root, root.sum()

    for child in root.children:
        temp, childSum = maxSumNode(child)
        if maxVal < childSum:
            maxNode = temp
            maxVal = childSum

    return maxNode, maxVal

root=takeTreeInputLevelWise()
printTreeDetailed(root)
mNode, mSum = maxSumNode(root)
print('Max Node = ', mNode)
print('Max sum = ', mSum)