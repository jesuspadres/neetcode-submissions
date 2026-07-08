class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        skipped = 0

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipped += 1
                right -= 1
            else:
                left += 1
                right -= 1

            

        if skipped <= 1:
            return True

        skipped = 0

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipped += 1
                left += 1
            else:
                left += 1
                right -= 1

            if skipped > 1:
                return False

        return True


