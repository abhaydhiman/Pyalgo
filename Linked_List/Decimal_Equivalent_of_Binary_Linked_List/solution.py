class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def insert(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.rear = self.head = temp
            return
        
        prev_node = self.rear
        self.rear.next = temp
        self.rear = temp
        self.rear.prev = prev_node
    
    def to_decimal(self):
        temp = self.rear
        power = 0
        decimal_form = 0
        
        while temp:
            res = temp.data * (2 ** power)
            decimal_form += res
            power += 1
            temp = temp.prev
        
        print(decimal_form)
        return

def display(Node, rev=False):
    if rev:
        temp = Node.rear
        
        while temp:
            print(temp.data, end=' ')
            temp = temp.prev
    else:
        temp = Node.head
        
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


ls = [0, 0, 0, 1, 1, 0, 0, 1, 0]

linked_list = LinkedList()

for i in ls:
    linked_list.insert(i)

display(linked_list)
print()
linked_list.to_decimal()