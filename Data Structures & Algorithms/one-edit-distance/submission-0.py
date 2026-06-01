class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        if abs(sLen - tLen) > 1:
            return False

        if sLen == tLen:
            diff = 0
            for i in range(sLen):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1

        long = s
        short = t

        if tLen > sLen:
            long = t
            short = s

        for i in range(len(long)):
            if (long[:i] + long[i+1:]) == short:
                return True

        return False