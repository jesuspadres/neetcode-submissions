class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        retVal = 0
        chars = {}
        lastDup = 0

        currCount = 0
        for i, c in enumerate(s):
            if c in chars:
                currCount = i - max(chars[c], lastDup)
                lastDup = max(chars[c], lastDup)
            else:
                currCount += 1
            chars[c] = i
            retVal = max(retVal, currCount)

        return retVal