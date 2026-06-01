class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        counts = [0 for _ in range(26)]

        for i in s:
            idx = ord(i) - ord('a') 

            counts[idx] += 1

        odds = 0

        for i in counts:
            if i % 2 == 1:
                odds += 1

        return odds <= 1