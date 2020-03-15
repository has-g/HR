class Stack(object):
    def __init__(self):
        # initialise an empty list called items
        self.items = []

    def push(self, item):
        # insert a new item by adding to the end, use append
        self.items.append(item)

    def pop(self):
        # if list is empty return None
        if not self.items:
            return None
        # pop the last item
        return self.items.pop()

    def peek(self):
        # if list is empty return None
        if not self.items:
            return None
        # report the last item in the list
        return self.items[-1]

class MaxStack(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        return super().push(item)

    def pop(self):
        return super().pop()

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)

a = MaxStack()
a.push(-1)
a.push(2)
a.push(-100)
a.push(20)

print(a.get_max())
print(a.pop())
print(a.get_max())
print(a.peek())


