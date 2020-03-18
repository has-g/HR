# 0, 1, 1, 2, 3, 5, 8, 13, ....
# f(n) = f(n-2) + f(n-1)
#

def fib(n):
    global fib_counter
    fib_counter += 1
    # edge case -ve
    if n < 0: raise IndexError('number cannot be negative')
    # edge cases 0
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

fib_counter = 0
print(fib(7))
print("fib_counter = ", fib_counter)

# total runtime is a binary tree due to recursion O(2**n)
# it is a binary tree of depth 5 for f(5)
# with memoization we can get to O(n) runtime and O(n) space
# use a dictionary so that lookup is also done at O(1) time

# two ways to do it - we can have a global variable declared and that accessed inside our function
# or define it as a class and use a class variable

def fib_m(n):
    global fib_counter
    fib_counter += 1
    # edge case -ve
    if n < 0: raise IndexError('number cannot be negative')
    # edge cases 0
    if n <= 1:
        return n

    global dDict
    a = 0

    if n in gDict:
        return gDict[n]
    else:
        a = fib_m(n-1) + fib_m(n-2)
        gDict[n] = a

    return a

gDict = {}
fib_counter = 0
print(fib_m(7))
print("fib_counter = ", fib_counter)


class fib_class:
    def __init__(self):
        self.dict = {}
        self.counter = 0

    def fib_class_fib(self, n):
        self.counter += 1
        #print("self.counter = ", self.counter)
        if n < 0: raise IndexError('number cannot be negative')
        if n <= 1:
            return n

        if n in self.dict:
            return self.dict[n]
        else:
            self.dict[n] = self.fib_class_fib(n-1) + self.fib_class_fib(n-2)

        return self.dict[n]

a = fib_class()
print(a.fib_class_fib(2))