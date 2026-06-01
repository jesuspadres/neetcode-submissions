class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            node = curr.children.get(c, TrieNode())
            curr.children[c] = node
            curr = node
        curr.end = True

    def search(self, word: str) -> bool:

        def helper(currRoot, word):
            if len(word) == 1:
                if word == ".":
                    for node in currRoot.children.values():
                        if node.end:
                            return True
                    return False
                elif word in currRoot.children:
                    return currRoot.children[word].end

            c = word[0]
            print(c)
            retVal = False
            if c == '.':
                for node in currRoot.children.values():
                    retVal = retVal or helper(node, word[1:])
            elif c in currRoot.children:
                retVal = helper(currRoot.children[c], word[1:])

            return retVal

        return helper(self.root, word)

        


                