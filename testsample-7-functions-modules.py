'''
nicer way of doing import of modules, create a library
and then import modules or parts of modules
with sys.path.append
'''

import sys
if '/Users/eshimpo/PycharmProjects/MyPythonModules' not in sys.path:
    sys.path.append('/Users/eshimpo/PycharmProjects/MyPythonModules')

# then import functions from within the module file
from checkifprime import isprime

def sumof_list(*args):
    sum = 0
    for i in args:
        sum += i
    return(sum)

def sumof_ages(**args):
    sum = 0
    for x, y in args.items():
        print('Name = %s, Age = %s' %(x, y))
        sum += y
    return(sum)


print(sumof_list(1, 2, 3, 4, 5))

print(sumof_ages(Mia = 9, Sami = 4))

print(isprime(13)) # note since import of one function was done, there was no need to prepend function with . operator


