from collections import deque

stack = deque()


stack.append("akabaka")
stack.append("takanaka")
stack.append("dakajaka")
stack.append("fakamaka")
print(stack)

class Stack:
    def __init__(self):
        self.container =[]
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def show(self):
        return self.container
    
s =Stack()

s.push("takanaka")
s.push("dakajaka")
s.push("fakamaka")
print(s.show())
print(s.peek())
print(s.is_empty())
print(s.size())
print(s.pop())
