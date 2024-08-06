class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        return self.queue

stack = Stack()
queue = Queue()

stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack.display())
print("Popped from stack:", stack.pop())
print("Stack after pop:", stack.display())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())
print("Dequeued from queue:", queue.dequeue())
print("Queue after dequeue:", queue.display())