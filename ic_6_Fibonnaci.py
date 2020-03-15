
#
# 0, 1, 1, 2, 3, 5, 8
# so fib(5) = fib(3) + fib(2)
#    fib(n) = fib(n-1) + fib(n-2)

# option1: just a recursive call will give us the value, check for negative, 0 and 1
def fib(n):
    if n < 0:
        print('-ve value not allowed')
        return None

    if n == 0 or n == 1: return n

    print('fib(' + str(n) + ') called')
    return fib(n-2) + fib(n-1)

print(fib(5))
print(fib(-2))

## for fib(5), we see fib(2) gets called thrice. One way is to store the value in a dictionary
# dict lookup is optimal as it will be done in O(1) time and it can be returned not computed

# two ways:
# Option2 = store in global variable outside the def call



mylist = {}

def fib(n):
    if n == 0 or n == 1:
        return n
    # define global inside def to reference something outside of it
    global mylist
    a, b = 0, 0
    print("mylist = ", mylist)

    if n in mylist:
        a = mylist[n]
    else:
        mylist[n] = fib(n - 1) + fib(n - 2)
        print('mylist inside = ', mylist)

    return mylist[n]

print(fib(6))
#print(fib(2))


class Fibonnaci:
    def __init__(self):
        self.mydict = {}

    def fibo(self, n):

        if n < 0:
            raise IndexError('index is negative')

        if n == 0 or n == 1:
            return n

        if n in self.mydict:
            a = self.mydict[n]
        else:
            self.mydict[n] = self.fibo(n - 1) + self.fibo(n - 2)
            print('mydict inside = ', self.mydict)

        return self.mydict[n]

f = Fibonnaci()
print(f.fibo(8))