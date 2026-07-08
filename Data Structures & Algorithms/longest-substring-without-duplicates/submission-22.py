class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        cache = {}

        left = right = 0
        retVal = 0

        while right < len(s):
            cache[s[right]] = cache.get(s[right], 0) + 1
            while cache.get(s[right], 0) > 1:
                cache[s[left]] -= 1
                left += 1

            retVal = max(retVal, 1 + right - left)
            right += 1

        return retVal
