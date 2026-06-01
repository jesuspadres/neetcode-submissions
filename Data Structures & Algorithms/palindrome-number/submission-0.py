class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        denom = 10
        digits = 0

        while x//denom > 0:
            digits += 1
            denom *= 10

        for i in range((digits//2)+1):
            denom = pow(10, digits)

            if (x // denom) != x % 10:
                return False
            
            x = x//10
            x = x % pow(10, digits-1)
            digits -= 2

        return True

        