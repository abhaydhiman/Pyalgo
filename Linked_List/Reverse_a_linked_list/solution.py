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
    
    def reverse(self):
        curr_node = self.head
        prev_node = self.head
        next_node = self.head.next
        curr_node.next = None
        
        while next_node:
            curr_node = next_node
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            self.head = prev_node


def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()



linked_list = LinkedList()
linked_list.insert(4)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

display(linked_list)

linked_list.reverse()

display(linked_list)
