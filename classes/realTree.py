class RealTrie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def __str__(self):
        return f"{self.root}"

    def add(self, word):
        print(f"Word {word}")
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
        print(f"Current {current}, {current[self.endSymbol]}")
