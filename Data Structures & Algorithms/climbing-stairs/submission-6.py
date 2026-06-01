class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 4:
            return n

        arr = [0 for _ in range(31)]

        arr[2] = 2
        arr[3] = 3

        for i in range(4, n+1):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n]