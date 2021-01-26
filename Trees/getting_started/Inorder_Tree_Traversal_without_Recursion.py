class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None


def inOrder(root):
    current_node = root
    stack = []
    top = -1
    
    while True:
        if current_node is not None:
            stack.append(current_node)
            top += 1
            current_node = current_node.left
        
        elif current_node is None and top != -1:
            node = stack.pop()
            print(node.val, end=' ')
            top -= 1
            current_node = node.right
        
        elif current_node is None and top == -1:
            return


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
