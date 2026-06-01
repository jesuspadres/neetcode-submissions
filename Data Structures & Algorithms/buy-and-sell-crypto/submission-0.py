class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        retVal = 0

        for n in prices:
            retVal = max(retVal, n - lowest)

            lowest = min(lowest, n)

        return retVal