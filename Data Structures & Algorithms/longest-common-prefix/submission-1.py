class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWord = min(strs)

        for word in strs:
            while minWord and word[:len(minWord)] != minWord:
                minWord = minWord[:-1]

        return minWord