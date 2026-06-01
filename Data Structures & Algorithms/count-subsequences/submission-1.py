class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        retVal = 0

        def helper(si, ti):
            nonlocal s, t, cache, retVal

            if ti >= len(t):
                return 1
            if si >= len(s):
                return 0

            if (si, ti) in cache:
                return cache[(si, ti)]

            ways = 0
            if s[si] == t[ti]:
                ways += helper(si+1, ti+1)
            ways += helper(si+1, ti)

            cache[(si, ti)] = ways

            return ways

        return helper(0,0)






        retVal = [0]
        ogT = t

        self.helper(s, t, retVal, ogT, [])

        return retVal[0]

    def helper(self, s, t, retVal, ogT, subSeq):
        if ogT == "".join(subSeq): 
            retVal[0] += 1
            return

        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    subSeq.append(s[j])
                    self.helper(s[j+1:], t[i+1:], retVal, ogT, subSeq)
                    subSeq.pop(-1)


