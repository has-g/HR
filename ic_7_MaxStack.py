class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):
    def __init__(self):
        self.st = Stack()

    def get_stack_len(self):
        return len(self.st.items)

    def get_max(self):
        listlen = self.get_stack_len()

        if listlen == 0: return -1
        if listlen == 1: return self.st.items[0]

        high = self.st.peek()
        mylist = []
        for i in range(listlen):
            # pop out element, compare with low
            y = self.st.pop()

            if y > high: high = y
            mylist.append(y)
        print(mylist)

        # rebuild the original list that i destroyed
        for j in mylist[::-1]:
            self.st.push(j)
        # just for printing - not accessing private variable directly
        print(self.st.items)
        #print(max(self.st.items))
        return high


ms = MaxStack()
ms.st.push(3)
ms.st.push(4)
ms.st.push(5)
ms.st.push(6)
ms.st.push(7)
ms.st.push(8)

#print(ms.st.peek())
print('original stack = ' + str(ms.st.items))
print(ms.get_max())
'''
[3, 4, 5, 6, 7, 8]
    pop, push, peek

    newlist = []
    pop out something, peek

    compare

    add to newlist

    once done, repopulate with push

'''
