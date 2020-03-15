# https://www.youtube.com/watch?v=o6563NNbdtg


class Trie():
    head = {}

    def add(self, word):
        current = self.head

        for char in word:
            print(char)
            if char not in current:
                    current[char] = {}
            current = current[char]
            print(current)

        current['*'] = True
        print(current)

    def search(self, word):
        current = self.head

        for char in word:
            if char not in current:
                return False
            current = current[char]

        if '*' in current:
            return True
        else:
            return False



dict = Trie()
dict.add('hi')
#dict.add("hello")
#dict.add('hey')
print(dict.search('hi'))
print(dict.search('hello'))
print(dict.search('hey'))
print(dict.search('hell'))