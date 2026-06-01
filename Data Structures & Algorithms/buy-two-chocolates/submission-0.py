class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = 0
        min2 = 1

        for i in range(len(prices)):
            if prices[i] < prices[min1]:
                min2 = min1
                min1 = i
            elif prices[i] < prices[min2] and i != min1:
                min2 = i

        if prices[min1] + prices[min2] <= money:
            return money - (prices[min1] + prices[min2])

        return money