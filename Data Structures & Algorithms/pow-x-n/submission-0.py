class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x

        count = x
        for _ in range(1, abs(n)):
            count *= x

        return count
