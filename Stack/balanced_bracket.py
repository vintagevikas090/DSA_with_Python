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
                if s[-1] != i:
                    s.push(i)
                else:
                    s.pop()
# After processing, the stack will contain unmatched brackets
# Unbalanced brackets can either be '{' or '}'
    reversals = 0
    while stack:
        top1 = stack.pop()
        top2 = stack.pop()
        
        # If both are the same, like "{{" or "}}", one reversal is needed
        if top1 == top2:
            reversals += 1
        else:                           # ***
            # If they are different, like "{}" or "}{", two reversals are needed
            reversals += 2

#(***)
# this {} is not balanced, becz didn't occur consecutively in string -> that's why they are in the mismatch stack 
