class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = self.start = None
    
    def insert(self, item):
        temp = Node(item)
        
        if self.head == None:
            self.head = self.start = temp
            return
        self.head.next = temp
        self.head = temp
    
    def display(self, node=None):
        if not node:
            temp = self.start
        else:
            temp = node
        
        while temp:
            print(temp.data, end='')
            temp = temp.next
    
    def reverse(self):
        curr_node = self.start
        prev_node = self.start
        next_node = self.start.next
        curr_node.next = None
        
        while next_node:
            curr_node = next_node
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node = curr_node
        
        self.start, self.head = self.head, self.start
        return curr_node
    
    def addOne(self):
        self.reverse()
        temp = self.start
        res = temp.data + 1
        ans = res//10
        prev = False
        
        if ans < 1:
            carry = False
        else:
            carry = True
        
        while temp:
            if carry:
                if not prev:
                    ouch = temp.data + 1
                    prev = True
                else:
                    ouch = temp.data + 1
            else:
                if not prev:
                    ouch = temp.data + 1
                    prev = True
                else:
                    ouch = temp.data
            
            if ouch // 10 < 1:
                temp.data = ouch
                carry = False
            else:
                temp.data = 0
                carry = True
            temp = temp.next
        
        if self.head.data == 0:
            self.insert(1)
        self.reverse()


head = LinkedList()
head.insert(1)
head.insert(2)
head.insert(9)
head.insert(9)

print('-'*50)
print('Original Number:-  ', end=' ')
head.display()

print()
print('After Adding One:- ', end=' ')
head.addOne()
head.display()

print()
print('-'*50)
