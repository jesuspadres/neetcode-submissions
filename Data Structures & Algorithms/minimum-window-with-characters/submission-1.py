class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        retVal = ""

        sMap = {}
        tMap = {}
        for i in range(len(t)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        l = 0
        r = len(t) - 1
        while r < len(s):
            valid = True
            for k in tMap.keys():
                if tMap[k] > sMap.get(k, 0):
                    valid = False
                    break

            if valid:
                if len(retVal) > r-l or retVal == "":
                    retVal = s[l:r+1]
                sMap[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    sMap[s[r]] = 1 + sMap.get(s[r], 0)

        return retVal
