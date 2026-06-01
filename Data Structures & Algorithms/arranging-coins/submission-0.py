class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        retVal = 0

        while n >= count:
            retVal += 1
            n -= count
            count += 1

        return retVal