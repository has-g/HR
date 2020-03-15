"""

Love it! check out the trie structure on print currentnode command

https://www.youtube.com/watch?v=hjUJFjcrbR4
https://www.interviewcake.com/question/python/compress-url-list?course=fc1&section=system-design

we chose to use nested dictionaries. To determine if a given site has been visited,
we just call add_word(), which adds a word to the trie if it's not already there

We add a dict {} for root node and for every next_node we also have a dict {} created
for valid elements we create the dict elements


"""

# create a Trie structure with empty dict {}

class Trie(object):
    def __init__(self):
        self.rootnode = {}

    def addword(self, word):
        # if word is empty: return as nothing to add
        if word == '': return False

        # flag to track new word when added
        isnewword = False

        # set nextnode to root to start
        nextnode = self.rootnode

        # loop through all alphabets of word
        # if alphabet is not in nextnode dict, then create a placeholder (remember this is a {})
        # set next node to next alphabet, create if it doesn't exist
        # skip over existing alphabets
        for alphabet in word:
            if alphabet not in nextnode:
                isnewword = True
                nextnode[alphabet] = {} # create a placeholder for the new alphabet
            nextnode = nextnode[alphabet]

        # create a final delimiter to mark end of word
        if '*' not in nextnode:
            nextnode['*'] = {} # create the placeholder for the node

        return isnewword


    def doeswordexist(self, word):
        if word == '': return True

        currentnode = self.rootnode

        for alphabet in word:
            if alphabet not in currentnode:
                return False # word does not exist even if one alphabet fails
            currentnode = currentnode[alphabet]
        print(currentnode)
        if '*' not in currentnode: return False

        return True


y = Trie()
y.addword('wait')
y.addword('waiter')
y.addword('sell')
y.addword('seller')
print(y.doeswordexist('sel'))
print(y.doeswordexist('wonder'))
print(y.doeswordexist('waiter'))

"""
comes from seller structure where the next node is compared after s
{'e': 
     {'l': 
          {'l': 
               {'*': {}, 
                'e': {'r': 
                          {'*': {}}
                      }
                }
           }
      }
 }

"""
