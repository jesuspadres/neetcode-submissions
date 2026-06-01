class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(list(s))

        odds = 0

        for val in counts.values():
            if val % 2 == 1:
                odds += 1

        return odds < 2