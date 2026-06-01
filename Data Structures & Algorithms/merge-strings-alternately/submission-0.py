class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        retVal = ""

        i = 0

        while True:
            if len(word1) <= i:
                retVal += word2[i:]
                break
            elif len(word2) <= i:
                retVal += word1[i:]
                break
            else:
                retVal += word1[i] + word2[i]
                i += 1

        return retVal