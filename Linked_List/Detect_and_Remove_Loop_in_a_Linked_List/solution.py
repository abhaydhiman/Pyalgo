class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.traversed = False


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def detect_remove_loop(self):
        temp = self.head
        prev = self.head
        
        while temp:
            if temp.traversed == True:
                print("Loop Exist; Removed Successfully!!")
                prev.next = None
                return
            
            temp.traversed = True
            prev = temp
            temp = temp.next
        
        print("Loop Does Not Exist!!")

def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next



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

linked_list.detect_remove_loop()
display(linked_list)
print()
