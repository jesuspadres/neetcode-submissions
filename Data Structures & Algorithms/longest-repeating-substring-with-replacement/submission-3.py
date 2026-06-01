class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        retVal = 0

        maxVal = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxVal = max(maxVal, counts[s[r]])
            

            if r - l + 1 - maxVal > k:
                counts[s[l]] = counts.get(s[l], 1) - 1
                l += 1
                
            retVal = max(retVal, r - l + 1)

        return retVal