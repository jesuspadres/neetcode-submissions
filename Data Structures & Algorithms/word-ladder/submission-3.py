class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        class WordNode:
            def __init__(self, word):
                self.word = word
                self.children = []


        if endWord not in wordList:
            return 0
        
        def letterDiff(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1

            return diff

        wordNodes = [WordNode(word) for word in wordList]
        startNode = WordNode(beginWord)

        for i in range(len(wordList)):
            if letterDiff(beginWord, wordList[i]) == 1:
                startNode.children.append(wordNodes[i])
                wordNodes[i].children.append(startNode)

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if letterDiff(wordList[j], wordList[i]) == 1:
                    wordNodes[j].children.append(wordNodes[i])

        visited = set()
        que = deque()
        retVal = 0

        def bfs():
            nonlocal retVal
            if not que:
                return
            vals = que.popleft()
            wordNode = vals[0]
            pos = vals[1]
            if retVal != 0:
                return
            
            nonlocal endWord
            visited.add(wordNode)
            print(wordNode.word)

            if wordNode.word == endWord:
                retVal = pos
                return

            for child in wordNode.children:
                if child not in visited:
                    que.append([child, pos+1])

            bfs()

        que.append([startNode, 1])
        bfs()

        return retVal


