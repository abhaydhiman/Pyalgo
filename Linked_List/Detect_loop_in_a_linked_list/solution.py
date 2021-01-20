class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.traversed = False

class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None

def check_loop(node):
    temp = node.head
    
    if temp == None:
        print("Empty!!")
        return
    
    while temp:
        if temp.traversed:
            print("Loop Exist!!")
            return
        
        temp.traversed = True
        temp = temp.next
    
    print("Loop Does Not Exist!!")


def loop_using_hash(node):          # O(n) and O(n) in both time and space
    temp = node.head
    h = set()
    
    if temp == None:
        print("Empty!!")
        return
    
    while temp:
        if temp in h:
            print("Loop Exist!!")
            return
        
        h.add(temp)
        temp = temp.next
    print("Loop Does Not Exist!!")


linked_list = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)
fifth = Node(5)

linked_list.head = linked_list.rear = first
first.next = second
second.next = third
third.next = forth
forth.next = fifth
fifth.next = second

check_loop(linked_list)
loop_using_hash(linked_list)
