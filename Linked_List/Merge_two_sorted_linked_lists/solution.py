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
    
    def push(self, item):
        temp = Node(item)
        
        if self.head == None:
            self.head = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp


def display(node):
    temp = node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()


def SortedMerge(node_a, node_b):
    temp_a = node_a.head
    temp_b = node_b.head
    
    sorted_list = LinkedList()
    sorted_list.rear = None
    
    while temp_a and temp_b:
        if temp_a.data < temp_b.data:
            sorted_list.push(temp_a.data)
            temp_a = temp_a.next
        
        elif temp_b.data < temp_a.data:
            sorted_list.push(temp_b.data)
            temp_b = temp_b.next
        
        elif temp_b.data == temp_a.data:
            sorted_list.push(temp_a.data)
            temp_a = temp_a.next
            temp_b = temp_b.next
    
    while temp_a:
        sorted_list.push(temp_a.data)
        temp_a = temp_a.next
    
    while temp_b:
        sorted_list.push(temp_b.data)
        temp_b = temp_b.next
    
    return sorted_list



X = LinkedList()
X.insert(15)
X.insert(10)
X.insert(5)

y = LinkedList()
y.insert(20)
y.insert(3)
y.insert(2)

print('First Linked List:- ', end='  ')
display(X)

print('Second Linked List:- ', end=' ')
display(y)

result = SortedMerge(X, y)

print('After Sorting lists:-', end=' ')
display(result)
