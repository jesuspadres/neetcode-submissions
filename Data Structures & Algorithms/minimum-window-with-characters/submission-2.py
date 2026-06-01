class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def containsT(s, t):
            cache = {}

            for c in s:
                if c in cache:
                    cache[c] += 1
                else:
                    cache[c] = 1

            for c in t:
                if c in cache and cache[c] > 0:
                    cache[c] -= 1
                else:
                    return False

            return True

        retVal = s
        l = 0
        r = len(t)
        while r <= len(s) and l < len(s):
            if containsT(s[l:r], t):
                if len(retVal) > r-l:
                    retVal = s[l:r]
                l += 1
            else:
                r += 1

        if retVal == s and not containsT(s, t):
            return ""

        return retVal
