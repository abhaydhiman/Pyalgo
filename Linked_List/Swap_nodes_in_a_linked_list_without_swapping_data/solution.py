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

def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next

def nodeSwapper(node, x, y):
    temp = node.head
    temp_x = None
    temp_y = None
    prev = node.head
    
    while temp:
        if temp.data == x:
            temp_x = temp
            prev.next = temp.next
            prev_x = prev
        
        if temp.data == y and temp_x != None:
            temp_y = temp
            prev.next = temp.next
            
            # to swap node x into y position
            temp_x.next = prev.next
            prev.next = temp_x
            
            # to swap node y into x position
            temp_y.next = prev_x.next
            prev_x.next = temp_y
            
            return
        
        prev = temp
        temp = temp.next


linked_list = LinkedList()
linked_list.insert(14)
linked_list.insert(20)
linked_list.insert(13)
linked_list.insert(12)
linked_list.insert(15)
linked_list.insert(10)

print("The linked list:- ")
display(linked_list)
print('\n')

x = 12
y = 20

nodeSwapper(linked_list, x, y)

print("After Swapping:- ")
display(linked_list)
print()
