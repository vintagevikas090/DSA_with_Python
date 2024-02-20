'''For a given expression in the form of a string,
find if there exist any redundant brackets or not. 
It is given that the expression contains only rounded brackets or parenthesis 
and the input expression will always be balanced.

A pair of the bracket is said to be redundant when a sub-expression is surrounded 
by unnecessary or needless brackets.'''

class stack:
    def __init__(self):
        self.arr = []
        
    def isEmpty(self):
        return len(self.arr)==0
    
    def push(self, data):
        self.arr.append(data)
    
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr.pop()
        
    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def print_stack(self):
        for i in self.arr:
            print(i, end= " ")
            
def isClosingBracket(char):
    return char == ')'
            
def redundent(exp):
    s = stack()
    if len(exp)==0:
        return False
    for i in exp:
        if not isClosingBracket(i):
            s.push(i)
        else:
            count = 0
            while s.top()!='(':
                count+=1
                s.pop()
            s.pop()
            if count <= 1:
                return True
    return False

expression = input('Enter the expression you want to check: ')
result = redundent(expression)
print('OUTPUT: ')
if result:
    print('Redundent Expression')
else:
    print('Not Redundent Expression')
