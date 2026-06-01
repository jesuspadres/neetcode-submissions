class Solution:
    def longestPalindrome(self, s: str) -> str:
        retVal = ""

        for i in range(len(s)):
            left = i-1
            right = i+1
            curr = s[i]

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curr = s[left] + curr + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            if len(retVal) < len(curr):
                retVal = curr

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr = s[i] + s[i+1]
            else:
                continue
            
            left = i-1
            right = i+2

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curr = s[left] + curr + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            if len(retVal) < len(curr):
                retVal = curr

        return retVal