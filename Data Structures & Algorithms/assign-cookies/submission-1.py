class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gIdx = len(g)-1
        sIdx = len(s)-1

        retVal = 0

        while gIdx >= 0 and sIdx >= 0:
            if s[sIdx] >= g[gIdx]:
                retVal += 1
                sIdx -= 1
                gIdx -= 1
            else:
                gIdx -= 1

        return retVal