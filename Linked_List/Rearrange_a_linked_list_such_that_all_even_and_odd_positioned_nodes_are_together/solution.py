class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
        self.length = 0
    
    def insert(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.rear = self.head = temp
            self.length += 1
            return
        
        self.rear.next = temp
        self.rear = temp
        self.length += 1
    
    def separator(self):
        temp = self.head
        length = self.length
        count = 1
        
        while count < length:
            if count % 2 != 0:
                item = temp.next.data
                temp.next = temp.next.next
                self.insert(item)
            else:
                temp = temp.next
            count += 1

def display(Node):
    temp = Node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next


linked_list = LinkedList()

for i in range(1, 8):
    linked_list.insert(i)

display(linked_list)
print()

print('After Separation:- ')        # Currently O(n) in time and no extra space; linkedlist object.
linked_list.separator()
display(linked_list)
print()
