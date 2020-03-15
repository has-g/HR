mylist = ['hello', 'this', 'is', 'a', 'message', 'from', 'mars']

for index, elementname in enumerate(mylist): # see use of enumerate keyword for indexifying the list
    print(index, elementname)

myTuple = ('hello', 'this', 'is', 'a', 'message', 'from', 'mars')
for index, elementname in enumerate(myTuple):
    print('index element pair is %d %s' %(index, elementname))
    print('>>> element pair is {0:d} {1:s}'.format(index, elementname))


myDict = {'Dad':45, 'Mum':43, 'Daughter':9, 'Son':4}
for i in myDict:
    print(i)    # note dictionary is keyword based, unless you use that as index for the value

for i in myDict:
    print(i, myDict[i])

for i, j in myDict.items():
    print(i, j)