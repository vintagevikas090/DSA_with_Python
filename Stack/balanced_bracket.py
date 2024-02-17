'''For a given expression in the form of a string,
find the minimum number of brackets that can be reversed in order to make the expression balanced.
The expression will only contain curly brackets.

If the expression can't be balanced, return -1.'''

'''Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced.
Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket 
and hence will not be able to make the expression balanced and the output will be -1.'''

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

def countBracketReversals(exp):
    if len(exp) == 0:
        return -1
    s = stack()
    for i in exp:
        if i == '{':
            s.push()
        else:
            if s.isEmpty():
                s.push(i)
            else:
                
    if s.size() % 2 == 0:
        return s.size()/2
    else:
        return -1
