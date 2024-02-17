
class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0
    
    def push(self, val):
        self.stack.append(val)
        self.count += 1
        if len(self.max_stack)== 0 or val < self.max_stack[0]:
            self.max_stack.append(val)
            return
        if val > self.max_stack[0]:
            self.max_stack.insert(0, val)


    def pop(self):
        if self.isEmpty():
            return -1
        temp = self.stack.pop()
        if temp == self.max_stack[0]:
            self.max_stack.pop(0)
        self.count -= 1
        return temp
    
    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]
    
    def get_max(self):
        if self.isEmpty():
            return -1
        return self.max_stack[0]
    
    def print_stack(self):
        print(self.stack)


s = Stack()
s.push(2)
s.push(4)
s.push(6)
s.push(8)
s.push(3)
s.push(1)
s.print_stack()
print("Top element is: ", s.top())
print("Maximum element is: ", s.get_max())
s.pop()
s.print_stack()
print("After popping Top element is: ", s.top())
