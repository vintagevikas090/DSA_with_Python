    '''Convert Sorted array to BST'''

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
        

def Build_BST(arr):
    l = len(arr)
    mid_index = l//2
    mid = arr[mid_index]
    root = Node(mid)
    root.left = Build_BST(arr[:mid_index])
    root.right = Build_BST(arr[mid_index:])
    return root
    
values = [int(i) for i in input().split()]
root = Build_BST(values)
print_Tree(root)
