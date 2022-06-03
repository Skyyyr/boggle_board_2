# Indicies is messed up apparently, which causes this entire class to fail - TODO: DELETE THis
class Trie:
    def __int__(self):
        self.root = {}
        self.endSymbol = "*"

    # def __str__(self):
    #     return f"{self.root} {self.endSymbol}"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
