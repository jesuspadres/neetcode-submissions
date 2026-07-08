class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def valid(s1):
            for i in range(len(s1)//2):
                j = -1 - i

                if s1[i] != s1[j]:
                    return False

            return True


        if valid(s):
            return True

        for i in range(len(s)):
            newS = s[:i] + s[i+1:]

            if valid(newS):
                return True

        return False