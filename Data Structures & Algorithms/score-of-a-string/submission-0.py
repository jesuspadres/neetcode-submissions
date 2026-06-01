class Solution:
    def scoreOfString(self, s: str) -> int:
        retVal = 0

        prev = ord(s[0])

        for i in range(1, len(s)):
            curr = ord(s[i])

            retVal += abs(prev - curr)

            prev = curr

        return retVal