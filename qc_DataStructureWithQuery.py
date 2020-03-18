'''
Python program to design a DS that
supports following operations
in O(n) time:
a) Insert
b) Delete
c) Search

Is insert O(1) computation time
Is delete O(1) time
Element x is unique in the DS

We create a list for holding the data
We create a dictionary hash to keep the value of the elements and index of each in the list

a) to insert x:
check hash to see if x is present, return if present
add x to the end of the list
update hash with key=x, value=len(list)

b) to delete x:
[a b x d e]
if x is not present: return
check hash to see if x is present, read index
find element at the end of the list
swap x with element e at the end of list
del list [last index:]
hash[e] = index(x)

c) to search x:
search in hash at O(1) time
return value from hash

'''

class DataStructure(object):
    def __init__(self):
        self.mylist = []
        self.mydict = {}

    def add(self, x):
        # a) to insert x:
        # check hash to see if x is present, return if present
        if x in self.mydict:
            return

        # add x to the end of the list
        self.mylist.append(x)

        # update hash with key=x, value=len(list)
        self.mydict[x] = len(self.mylist) - 1

        print('list = ', self.mylist)
        print('dict = ', self.mydict)

    def remove(self, x):
        # b) to delete x:
        # [a b x d e]
        # if x is not present in dict: return
        if x in self.mydict:
            # check hash to see if x is present, read index
            idx = self.mydict[x]

            # find element at the end of the list
            lastelement = self.mylist[-1]
            print('last el = ', lastelement)
            # swap x with element e at the end of list
            self.mylist[idx], self.mylist[- 1] = self.mylist[- 1], self.mylist[idx]

            # del list [last index:]
            del self.mylist[-1]

            # hash[e] = index(x)
            self.mydict[lastelement] = idx

            # delete the old entry from hash as well
            del self.mydict[x]

            print('list = ', self.mylist)
            print('dict = ', self.mydict)
        else:
            return

    def search(self, x):
        # c) to search x:
        # search in hash at O(1) time
        if x in self.mydict:
            # return value from hash
            return self.mydict.get(x)
        else:
            return None


# Driver Code
if __name__=="__main__":
    ds = DataStructure()
    print("========= all adds ==============")
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    print("========= search 30 ==============")
    print(ds.search(30))
    print("========= remove 20 ==============")
    ds.remove(20)
    print("========= add 50 ==============")
    ds.add(50)
    print("========= search 50 ==============")
    print(ds.search(50))
