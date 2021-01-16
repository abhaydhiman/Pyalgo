class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

def Circular(Node):
    temp = Node.head
    
    if temp == None:
        return True
    
    res = temp.next
    
    while res and res is not temp:
        res = res.next
    
    return res == temp


linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)

linked_list.head.next = second
second.next = third
third.next = forth

if Circular(linked_list):
    print("yes")
else:
    print("No")

forth.next = linked_list.head

if Circular(linked_list):
    print("yes")
else:
    print("No")
