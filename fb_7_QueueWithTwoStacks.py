"""
This technique is super important

Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).
Optimize for the time cost of mm calls on your queue. These can be any mix of enqueue and dequeue calls.
Assume you already have a stack implementation and it gives O(1)O(1) time push and pop.

inQueue just adds to In Stack
deQueue just builds up the Out Stack and copies the last element from InStack
   it then pops out and returns the top value
   it then retains all the remaining element in out Stack

Notice that the more expensive a dequeue on an empty out_stack is
(that is, the more items we have to move from in_stack to out_stack),
the more O(1)O(1)-time dequeues off of a non-empty out_stack it wins us in the future.
Once items are moved from in_stack to out_stack they just sit there, ready
to be dequeued in O(1) time. An item never moves "backwards" in our data structure.
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.items: return None
        return self.items.pop()

    def peek(self):
        if not self.items: return None
        return self.items[-1]


class QueueTwoStacks(Stack):
    def __init__(self):
        self.stackIn = Stack()
        self.stackOut = Stack()

    def enQueue(self, item):
        return self.stackIn.push(item)


    def deQueue(self):
        # copy items from In to Out
        while len(self.stackIn.items) > 0:
            el = self.stackIn.pop()
            self.stackOut.push(el)

        # pop out top element from Out
        return self.stackOut.pop()

    def PeekIn(self):
        return self.stackIn.peek()

    def PeekOut(self):
        return self.stackOut.peek()

myQ = QueueTwoStacks()
myQ.enQueue(1)
myQ.enQueue(2)
myQ.enQueue(3)
print(myQ.PeekIn()) # should be 3
print(myQ.PeekOut()) # should be None
print(myQ.deQueue()) # should be 1
print(myQ.deQueue()) # should be 2
print(myQ.deQueue()) # should be 3
myQ.enQueue(4)
print(myQ.deQueue()) # should be 4
print(myQ.deQueue()) # should be None - all exhausted
print(myQ.PeekIn()) # should be None
print(myQ.PeekOut()) # should be None

