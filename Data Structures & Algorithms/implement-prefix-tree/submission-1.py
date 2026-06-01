class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        
        curr = self.root
        for c in word:
            curr.children[c] = curr.children.get(c, TrieNode())
            curr = curr.children[c]

        curr.end = True


    def search(self, word: str) -> bool:
        if not word:
            return True
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True
        