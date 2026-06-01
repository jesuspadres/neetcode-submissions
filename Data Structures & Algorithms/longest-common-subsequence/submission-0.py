class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        letters1 = set()
        commonChars = set()

        for c in text1:
            letters1.add(c)
        for c in text2:
            if c in letters1:
                commonChars.add(c)

        word1 = ""
        word2 = ""

        for c in text1:
            if c in commonChars:
                word1 += c

        for c in text2:
            if c in commonChars:
                word2 += c

        
        subseqs1 = set()
        for c in word1:
            newSet = set()
            for sub in subseqs1:
                newSet.add(sub)
                newSet.add(sub+c)
            newSet.add(c)
            subseqs1 = newSet

        retVal = 0
        subseqs2 = set()
        for c in word2:
            newSet = set()
            for sub in subseqs2:
                withC = sub+c
                newSet.add(sub)
                newSet.add(withC)
                if withC in subseqs1:
                    retVal = max(retVal, len(withC))
            newSet.add(c)
            if c in subseqs1:
                    retVal = max(retVal, 1)
            subseqs2 = newSet

        return retVal
