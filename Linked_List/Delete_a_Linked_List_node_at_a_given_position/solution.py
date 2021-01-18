class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def isEmpty(self):
        return self.head == None
    
    def insert(self, item):
        temp = Node(item)
        
        if self.head == None:
            self.head = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp
    
    def delete(self, index):
        if self.isEmpty():
            print('Empty linked list!!')
            return
        else:
            count = 0
            prev = self.head
            temp = self.head
            
            while temp:
                if count == index:
                    prev.next = temp.next
                    return
                count += 1
                prev = temp
                temp = temp.next


def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next


linked_list = LinkedList()
linked_list.insert(2)
linked_list.insert(4)
linked_list.insert(1)
linked_list.insert(9)
linked_list.insert(3)
linked_list.insert(7)

display(linked_list)
print()

linked_list.delete(2)

display(linked_list)
print()
