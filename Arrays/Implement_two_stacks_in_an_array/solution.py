class TwoStacks:
    def __init__(self, num):
        self.num = num
        self.arr = [None]*num
        self.top1 = -1
        self.top2 = num
    
    def push1(self, x):
        print('top1', self.top1)
        print('top2', self.top2)
        if (self.top1 + 1) >= self.top2:
            print("Overflow condition!")
        
        else:
            self.top1 += 1
            self.arr[self.top1] = x
    
    def push2(self, x):
        if self.top2 <= (self.top1 + 1):
            print("Overflow condition!")
        
        else:
            self.top2 -= 1
            self.arr[self.top2] = x
    
    def pop1(self):
        if self.top1 == -1:
            print("Underflow condition!")
        
        else:
            popped_item = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return popped_item
    
    def pop2(self):
        if self.top2 >= self.num:
            print("Underflow condition!")
        
        else:
            self.arr[self.top2] = None
            self.top2 += 1
    
    def display1(self):
        return self.arr[: (self.top1 + 1)]
    
    def display2(self):
        return self.arr[(self.top2): ]


# driver code
ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push1(12)
ts.push1(19)
ts.push2(7)
ts.push2(7)

print(ts.display1())
print(ts.display2())
