'''Given Inorder and PostOrder, Build the tree'''

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


def buildTree(postOrder, inOrder, n):
    if n<=0 :
        return None
    rootData = postOrder[-1]
    rootIndex = inOrder.index(rootData)
    left_data_of_root = inOrder[:rootIndex]
    right_data_of_root = inOrder[rootIndex+1:]
    left_nodes_no = len(left_data_of_root)
    right_nodes_no = n - left_nodes_no -1
    
    root = Node(rootData)
    root.left = buildTree(postOrder[:left_nodes_no],left_data_of_root , left_nodes_no)
    root.right = buildTree(postOrder[left_nodes_no:left_nodes_no+right_nodes_no] ,right_data_of_root, right_nodes_no)
    return root

print('Enter Inorder Expression: ')
exp_inorder = [int(i) for i in input().split()]
print('Enter Postorder Expression: ')
exp_postorder = [int(j) for j in input().split()]
print()


root = Build_tree(exp_postorder,exp_inorder, len(exp_inorder))
print_Tree(root)
