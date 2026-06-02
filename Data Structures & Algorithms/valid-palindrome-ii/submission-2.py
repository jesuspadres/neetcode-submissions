class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(word):
            return word == word[::-1]

        if isPalindrome(s):
            return True

        for i in range(len(s)):
            newS = s[:i] + s[i+1:]

            if isPalindrome(newS):
                return True


        return False

