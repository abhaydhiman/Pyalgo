class Queue:
    def __init__(self, range):
        self.range = range
        self.queue = [None]*self.range
        self.front = self.size = self.rear = 0
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def is_full(self):
        return self.size == self.range
    
    def display(self):
        if self.is_empty():
            print("Nothing to display; queue is empty")
            return
        
        for i in self.queue:
            if i:
                print(i, end=' ')
        return
    
    def enqueue(self, ele):
        if self.is_full():
            print('Queue is full')
            return
        
        self.queue[self.rear] = ele
        self.rear += 1
        self.size += 1
        print('Element enqueued successfully!!')
        return
    
    def dequeue(self):
        if self.is_empty():
            print('Queue is already empty!!')
            return
        
        self.queue[self.front] = None
        temp = 0
        
        while temp < (self.size - 1):
            self.queue[temp], self.queue[temp + 1] = self.queue[temp + 1], self.queue[temp]
            temp += 1
        
        self.size -= 1
        self.rear -= 1
        print('Element dequeued successfully!!')
    
    def que_front(self):
        if self.is_empty():
            print("Queue is empty!!")
            return
        
        print("Front element is:- ", self.queue[self.front])
    
    def que_rear(self):
        if self.is_empty():
            print('Queue is empty!!')
            return
        
        print('Rear element is:- ', self.queue[self.rear - 1])



obj = Queue(20)
obj.enqueue(2)
obj.enqueue(5)
obj.dequeue()
obj.enqueue(7)
obj.enqueue(45)
obj.enqueue(10)
obj.display()
print()
obj.que_front()
obj.que_rear()
