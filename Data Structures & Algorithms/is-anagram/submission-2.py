class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}

        for c in s:
            if c in cache:
                cache[c] += 1
            else:
                cache[c] = 1

        for c in t:
            if c not in cache:
                return False
            else:
                cache[c] -= 1

        for v in cache.values():
            if v != 0:
                return False

        return True