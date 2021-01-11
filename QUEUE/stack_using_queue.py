class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SQueue:
    def __init__(self) -> None:
        self.front = self.rear = None
    
    def push(self, ele):
        temp = Node(ele)
        
        if self.rear == None:
            self.rear = self.front = temp
            return
        
        self.rear.next = temp
        self.rear = temp
    
    def is_empty(self):
        return self.front == None
    
    def display(self):
        temp = self.front
        
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
    
    def pop(self):
        if self.is_empty():
            print("empty!!")
            return
        
        temp = self.front
        while True:
            if temp.next == self.rear:
                break
            temp = temp.next
            
        
        self.rear = temp
        self.rear.next = None


obj = SQueue()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
obj.pop()
obj.display()
