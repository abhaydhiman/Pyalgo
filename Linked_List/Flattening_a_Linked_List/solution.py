class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.down = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def insert(self, item, location):
        temp = Node(item)
        
        if self.rear == None:
            self.head = self.rear = temp
            return
        
        if 'right' in location.lower():
            self.rear.right = temp
            self.rear = temp
            return
        
        if 'down' in location.lower():
            temp.down = self.rear.down
            self.rear.down = temp
            return



def sortedMerge(a, b):
    result = None
    
    if a == None:
        return b
    if b == None:
        return a
    
    if a.data <= b.data:
        result = a
        result.down = sortedMerge(a.down, b)
    else:
        result = b
        result.down = sortedMerge(a, b.down)
    
    result.right = None
    return result


def flatter(node):
    if node == None or node.right == None:
        return node
    
    return sortedMerge(node, flatter(node.right))


def display(Node):
    temp = Node.head
    
    while temp:
        print(temp.data, end=' ==> ')
        temp_down = temp.down
        
        while temp_down:
            print(temp_down.data, end=' ---> ')
            temp_down = temp_down.down
        temp = temp.right


linked_list = LinkedList()
linked_list.insert(5, 'right')
linked_list.insert(30, 'down')
linked_list.insert(8, 'down')
linked_list.insert(7, 'down')
linked_list.insert(10, 'right')
linked_list.insert(20, 'down')
linked_list.insert(19, 'right')
linked_list.insert(50, 'down')
linked_list.insert(22, 'down')
linked_list.insert(28, 'right')
linked_list.insert(45, 'down')
linked_list.insert(40, 'down')
linked_list.insert(35, 'down')


display(linked_list)
print()

flatter(linked_list.head)

display(linked_list)
print()