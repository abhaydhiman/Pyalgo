class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

class AvlTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        if balance > 1 and key < root.left.val:
            return self.rightRotation(root)
        
        elif balance < -1 and key > root.right.val:
            return self.leftRotation(root)
        
        elif balance > 1 and key > root.left.val:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        
        elif balance < -1 and key < root.right.val:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
        
        return root
    
    def getHeight(self, root):
        if root is None:
            return 0
        return root.height
    
    def preOrder(self, root):
        if root is None:
            return
        else:
            print(root.val, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotation(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
    
    def rightRotation(self, z):
        y = z.left
        T2 = y.right
        
        y.right = z
        z.left = T2
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y



avl_tree = AvlTree()
root = None

root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)
root = avl_tree.insert(root, 40)
root = avl_tree.insert(root, 50)
root = avl_tree.insert(root, 25)

avl_tree.preOrder(root)
print()

print(root.height)
