class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cache = Counter(s)
        print(cache)

        for c in t:
            if cache.get(c, 0) == 0:
                return c
            else:
                cache[c] -= 1
            