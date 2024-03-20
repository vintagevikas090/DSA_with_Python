class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Initialize an empty tree with no nodes
        self.root = None
        self.numNodes = 0  # Track the number of nodes in the tree
    
    # Helper function to print the tree recursively
    def printTreeHelper(self, root):
        if root == None:
            return
        # Print the current node and its left and right children if present
        print(root.data, end=":")
        if root.left != None:
            print("L:", end='')
            print(root.left.data, end=',')
        if root.right != None:
            print("R:", end='')
            print(root.right.data, end='')
        print()
        
        # Recursively call on left and right subtrees
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    # Public function to print the tree
    def printTree(self):
        self.printTreeHelper(self.root)
    
    # Helper function to check if a given data is present in the tree
    def isPresentHelper(self, root, data):
        if root == None:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:
            # Call on the left subtree
            return self.isPresentHelper(root.left, data)
        else:
            # Call on the right subtree
            return self.isPresentHelper(root.right, data)
    
    # Public function to search for a data in the tree
    def search(self, data):
        return self.isPresentHelper(self.root, data)

    # Helper function to insert a new node with given data
    def insertHelper(self, root, data):
        if root == None:
            # Create a new node if the current node is None
            node = Node(data)
            return node
        
        if root.data >= data:
            # Insert in the left subtree
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            # Insert in the right subtree
            root.right = self.insertHelper(root.right, data)
            return root
    
    # Public function to insert a new node with given data
    def insert(self, data):
        self.numNodes += 1  # Increment the node count
        self.root = self.insertHelper(self.root, data)
    
    # Helper function to find the minimum value node in a subtree
    def min(self, root):
        if root == None:
            return 10000  # A large value indicating an empty subtree
        
        if root.left == None:
            return root.data
        
        return self.min(root.left)
    
    # Helper function to delete a node with given data
    def deleteDataHelper(self, root, data):
        if root == None:
            return False, None  # Data not found, return False and None
        
        if root.data < data:
            # Delete in the right subtree
            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            # Delete in the left subtree
            deleted, newLeftNode = self.deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        # Node to be deleted is a leaf
        if root.left == None and root.right == None:
            return True, None  # Indicate successful deletion and None as the replacement
        
        # Node to be deleted has one child
        if root.left == None:
            return True, root.right  # Indicate successful deletion and the right child as the replacement
        
        if root.right == None:
            return True, root.left  # Indicate successful deletion and the left child as the replacement
        
        # Node to be deleted has two children
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, root
        
    # Public function to delete a node with given data
    def delete(self, data):
        deleted, newRoot = self.deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1  # Decrement the node count
        self.root = newRoot
        return deleted
    
    # Public function to get the count of nodes in the tree
    def count(self):
        return self.numNodes
    
b=BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()
print(b.count())
b.delete(10)
b.printTree()