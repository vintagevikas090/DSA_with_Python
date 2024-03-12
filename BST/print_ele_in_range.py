    '''Print element in a given range of k1 and k2'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_Tree(root):
    if root is None:
        return 
    q = [root]
    while q:
        curr = q.pop(0)
        print(curr.data, end = ":")
        
        if curr.left is not None:
            leftData = curr.left.data
            print('L:', leftData ,end=",")
            q.append(curr.left)
        else:
            print('L:-1', end = ',')
            
        if curr.right is not None:
            rightData = curr.right.data
            print("R:", rightData, end = "")
            q.append(curr.right)
        else:
            print('R:-1', end = "")

        print()
        
def insert_in_BST(root, val):
    if val == -1:
        return None
    newNode = Node(val)
    if root == None:
        root = newNode
        return root
    if val <= root.data:
        root.left = insert_in_BST(root.left, val)
    else:
        root.right = insert_in_BST(root.right, val)
    return root

def Build_BST(li):
    rootData = li[0]
    root = Node(rootData)
    for i in li[1:]:
        root = insert_in_BST(root, i)
    return root

def print_ele_between_k1_and_k2(root, k1, k2):
    if root==None:
        return
    if k1<=root.data and root.data<=k2:
        print_ele_between_k1_and_k2(root.left, k1, k2)
        print(root.data, end=' ')
        print_ele_between_k1_and_k2(root.right, k1, k2)
        return
    if root.data>k2:
        print_ele_between_k1_and_k2(root.left, k1, k2)
    else:
        print_ele_between_k1_and_k2(root.right, k1, k2)
    
print('Enter the values you want to insert in Tree(space Seperated): ')
values = [int(i) for i in input().split()]
root = Build_BST(values)
print_Tree(root)
print_ele_between_k1_and_k2(root, 2, 10)