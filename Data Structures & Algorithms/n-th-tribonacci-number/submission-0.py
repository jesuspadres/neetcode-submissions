class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1

        t0 = 0
        t1 = t2 = 1
        curr = 0

        for i in range(2, n):
            curr = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = curr

        return curr