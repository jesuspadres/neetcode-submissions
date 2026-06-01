class Solution:
    def validPalindrome(self, s: str) -> bool:
        diff = 0
        retVal = True

        j = -1
        for i in range((len(s)+1)//2):
            if s[i] != s[j]:
                diff += 1
            else:
                j -= 1

            if diff > 1:
                retVal = False

        diff = 0

        j = 0
        for i in range(1, (len(s)+1)//2 + 1):
            if s[-i] != s[j]:
                diff += 1
            else:
                j += 1

            if diff > 1:
                return retVal or False

        return True
