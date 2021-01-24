class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)

print(height(root))



# ----------------------------
# Understanding recursion
# ----------------------------


# def lsCounter(value):
#     if value == 5:
#         return 0
#     else:
#         count = lsCounter(value + 1)
#         # print('v', value)
#         print(count)
#         return count + 1

# lsCounter(1)
