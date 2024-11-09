from nodeTree import NodeTree

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def insert(self, node: NodeTree, data):
        if self.isEmpty():
            self.root = NodeTree(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            if data > node.data:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)
                    
    def search(self, node: NodeTree, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
        
    def printInOrder(self, node: NodeTree):
        if self.isEmpty():
            print("Empty tree!")
        else:
            if node is not None:
                if node.left:
                    self.printInOrder(node.left)
                print(f"{node.data}\n")
                if node.right:
                    self.printInOrder(node.right)
                
    def printPreOrder(self, node):
        if self.isEmpty():
            print("Empty tree!")
        else:
            if node is not None:
                print(f"{node.data}\n")
                if node.left:
                    self.printPreOrder(node.left)
                if node.right:
                    self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if self.isEmpty():
            print("Empty tree!")
        else:
            if node is not None:
                if node.left:
                    self.printPostOrder(node.left)
                if node.right:
                    self.printPostOrder(node.right)
                print(f"{node.data}\n")
    
    def minNode(self, node: NodeTree):
        if self.isEmpty():
            print("Empty list!")
        else:
            while node.left:
                node = node.left
            return node.data
        
    def maxNode(self, node: NodeTree):
        if self.isEmpty():
            print("Empty tree!")
        else:
            while node.right:
                node = node.right
                
            return node.data
        
    def heightTree(self, node: NodeTree):
        if node:
            return 1 + max(self.heightTree(node.left), self.heightTree(node.right))
        else:
            return 0
    
    def countNodes(self, node: NodeTree):
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
    
    def _minValueRight(self, node: NodeTree):
        current = node
        while current.left is not None:
            current = current.left
            return current
    
    def delete(self, node: NodeTree, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            # Case 1: The node to be deleted has no children (leaf node)
            if node.left is None and node.right is None:
                return None
            # Case 2: The node to be deleted has only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: The node to be deleted has two children
            else:
                # Find the node with the minimum value in the right subtree
                successor = self._minValueRight(node.right)
                node.data = successor.data
                # Delete successor
                node.right = self.delete(node.right, successor.data)
        return None                
    
    def printTree(self, node: NodeTree, level):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level + 1)
    
    def deleteTree(self):
        self.root = None