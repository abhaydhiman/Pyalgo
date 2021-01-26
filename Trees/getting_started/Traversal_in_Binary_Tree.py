class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None


def printInorder(node):
    if node == None:
        return
    
    else:
        printInorder(node.left)
        print(node.val, end=' ')
        
        right_node = printInorder(node.right)
        
        if right_node is not None:
            print(right_node.val, end=' ')


def preOrder(node):
    if node == None:
        return
    else:
        print(node.val, end=' ')
        left_node = preOrder(node.left)
        
        right_node = preOrder(node.right)
        if right_node is not None:
            print(right_node.val, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

printInorder(root)
print()

preOrder(root)
