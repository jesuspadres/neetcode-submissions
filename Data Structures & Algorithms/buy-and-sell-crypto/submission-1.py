class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buys = []

        smallest = prices[0]

        for i in prices:
            smallest = min(smallest, i)

            buys.append(smallest)

        retVal = 0

        for i in range(len(prices)-1, -1, -1):
            retVal = max(retVal, prices[i] - buys[i])

        return retVal