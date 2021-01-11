class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self, ele):
        print(f"Element {ele} is enqueued!!")
        temp = Node(ele)
        
        if self.rear == None:
            self.rear = self.front = temp
            return
        
        self.rear.next = temp
        self.rear = temp
    
    def dequeue(self):
        if self.is_empty():
            print("Empty empty!!")
            return
        
        print(f"Element {self.front.data} is dequeued!!")
        self.front = self.front.next
        
        if self.front == None:
            self.rear = None
    
    def display(self):
        temp = self.front
        
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        
        return


obj = Queue()
obj.enqueue(20)
obj.enqueue(70)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(10)
obj.dequeue()
obj.display()
