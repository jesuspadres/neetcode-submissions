class Solution:
    def numDistinct(self, s: str, t: str) -> int:
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


