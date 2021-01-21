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

def add(temp_a, temp_b, carry):
    
    if temp_a and temp_b:
        result = None
        data_a = temp_a.data
        data_b = temp_b.data
        
        sum = data_a + data_b
        
        if sum > 9 or carry > 0:
            sum += carry
            carry = sum // 10
            sum = sum % 10
        
        temp = Node(sum)
        temp.next = result
        result = temp
        print(result.data, end=' ')
        
        add(temp_a.next, temp_b.next, carry)
        
    else:
        return

ll_a = LinkedList()
ll_a.insert(3)
ll_a.insert(6)
ll_a.insert(5)

print("Linked list for first number:- ")
display(ll_a)
print()

ll_b = LinkedList()
ll_b.insert(2)
ll_b.insert(4)
ll_b.insert(8)

print("Linked list for second number:- ")
display(ll_b)
print('\n')

add(ll_a.head, ll_b.head, 0)
