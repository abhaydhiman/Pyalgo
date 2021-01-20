class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def insert(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.rear = self.head = temp
            return
        
        self.rear.next = temp
        self.rear = temp
    
    def printRev(self, temp):
        if temp:
            self.printRev(temp.next)
            print(temp.data, end=' ')
        else:
            return
    
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


linked_list = LinkedList()
linked_list.insert(4)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

linked_list.display()
print()
linked_list.printRev(linked_list.head)
