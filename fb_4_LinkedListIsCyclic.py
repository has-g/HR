class LinkedListNode(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def islistcyclic(firstnode):
    fastrunner = firstnode
    slowrunner = firstnode

    # fast runner goes twice as fast as slow until it catches up
    # if reaches the tail == None , then it is not cyclic
    while (fastrunner != None) and (slowrunner != None):
        slowrunner = slowrunner.next
        fastrunner = fastrunner.next.next

        if slowrunner is fastrunner:
            return True

    return False


d = LinkedListNode(4, None)
c = LinkedListNode(3, d)
b = LinkedListNode(2, c)
a = LinkedListNode(1, b)
print(islistcyclic(a))

fourth = LinkedListNode(4)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)
fourth.next = first
print(islistcyclic(first))
