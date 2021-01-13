class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.rear = None
    
    def insert(self, item):
        temp = Node(item)
        
        if self.rear == None:
            self.rear = self.head = temp
            return
        
        self.rear.next = temp
        self.rear = temp
    
    def length(self):
        temp = self.head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        return count
    
    def deleter(self, m, n):
        # length = self.length()
        
        # if (m + n) > length:
        #     print('Invalid!!')
        #     return
        
        temp = self.head
        count_m = 1
        count_n = 0
        
        while temp:
            if count_m != m and (temp.next != None):
                count_m += 1
                temp = temp.next
            else:
                if count_n != n and (temp.next != None):
                    temp.next = temp.next.next
                    count_n += 1
                else:
                    temp = temp.next

def display(Node):
    temp = Node.head
    
    while temp:
        print(temp.data, end=' ')
        temp = temp.next


linked_list = LinkedList()

for i in range(10, 0, -1):
    linked_list.insert(i)

linked_list.deleter(3, 10)

display(linked_list)
