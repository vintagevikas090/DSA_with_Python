'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.'''

class MinStack:

    def __init__(self):
        self.stack = []     

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


'''Optimised Code'''
   
class MinStack:

    def __init__(self):
        self.stack = []     
        self.min_stack = []  

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)==0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

