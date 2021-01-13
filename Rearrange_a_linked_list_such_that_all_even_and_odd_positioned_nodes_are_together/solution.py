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
        ls = [None]*self.length
        mid = (self.length // 2) + (self.length % 2)
        start = 0
        temp = self.head
        count = 1
        
        while temp:
            if count % 2 == 0:
                ls[mid] = temp.data
                mid += 1
            else:
                ls[start] = temp.data
                start += 1
            temp = temp.next
            count += 1
        
        for i in ls:
            print(i, end=' ')

def display(Node):
    temp = Node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next


linked_list = LinkedList()

for i in range(1, 7):
    linked_list.insert(i)

display(linked_list)
print()

print('After Separation:- ')        # Currently O(n) in both time and space; not of linked list object.
linked_list.separator()
