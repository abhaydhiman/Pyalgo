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


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)
root.right.left = Node(50)

printInorder(root)
