class Solution:
    def countSubstrings(self, s: str) -> int:
        retVal = 0

        for i in range(len(s)):
            left = i-1
            right = i+1
            curr = s[i]
            retVal += 1

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    retVal += 1
                    curr = s[left] + curr + s[right]
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr = s[i] + s[i+1]
                retVal += 1
            else:
                continue
            
            left = i-1
            right = i+2

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    retVal += 1
                    curr = s[left] + curr + s[right]
                    left -= 1
                    right += 1
                else:
                    break

        return retVal