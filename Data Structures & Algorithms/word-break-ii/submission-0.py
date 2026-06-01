class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        retList = []
        wordDict = set(wordDict)
        cache = {}
        
        def helper(currS):
            if not currS:
                return ["1"]
            if currS in cache:
                return cache[currS]

            words = []
            for i in range(len(currS)):
                if currS[:i+1] in wordDict:
                    for word in helper(currS[i+1:]):
                        newWord = currS[:i+1] + " " + word
                        
                        if newWord[-1] == "1":
                            words.append(newWord)
            cache[currS] = words

            return words

        for sentence in helper(s):
            retList.append(sentence[:-2])

        return retList
