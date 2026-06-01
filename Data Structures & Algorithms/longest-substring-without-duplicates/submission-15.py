class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        cache = set()
        maxVal = 1

        l = 0
        r = 1

        cache.add(s[l])
        while r < len(s):
            maxVal = max(maxVal, len(cache))
            if s[r] in cache:
                while s[r] in cache:
                    cache.remove(s[l])
                    l += 1
            
            cache.add(s[r])
            r += 1

        return max(maxVal, len(cache))