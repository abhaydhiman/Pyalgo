class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, item):
        temp = Node(item)
        
        temp.next = self.head
        self.head = temp
    
    def middleFinder(self):
        slow = self.head
        fast = self.head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.data)


def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()



linked_list = LinkedList()

for i in range(5, 0, -1):
    linked_list.insert(i)

display(linked_list)

linked_list.middleFinder()
