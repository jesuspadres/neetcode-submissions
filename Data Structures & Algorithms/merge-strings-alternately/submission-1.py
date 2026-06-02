class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        retVal = ""

        while len(word1) > 0 or len(word2) > 0:
            if len(word1) > 0:
                retVal += word1[0]
                word1 = word1[1:]

            if len(word2) > 0:
                retVal += word2[0]
                word2 = word2[1:] 

        return retVal