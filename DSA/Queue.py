from collections import deque
stack = deque()

stack.appendleft("tingting")
stack.appendleft("singsing")
stack.appendleft("fingting")
print(stack)


# Doing with class
from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

s = Queue()
s.enqueue({
    'company': 'Wal Mart',
    'timestamp': '9.45 PM',
    'price': 120
})
s.enqueue({
    'company': 'Aple',
    'timestamp': '9.46 PM',
    'price': 130
})
s.enqueue({
    'company': 'Samsung',
    'timestamp': '9.47 PM',
    'price': 140
})
print(s.buffer)
print(s.dequeue())