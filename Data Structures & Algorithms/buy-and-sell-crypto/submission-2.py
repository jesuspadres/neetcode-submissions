class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = prices[0]


        retVal = 0

        for i in range(len(prices)):
            smallest = min(smallest, prices[i])
            retVal = max(retVal, prices[i] - smallest)

        return retVal