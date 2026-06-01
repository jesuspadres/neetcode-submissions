class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        capProfits = {}

        def helper(index, profit, weight, capacity):
            if capacity == 0 or index >= len(profit):
                return 0
            if capacity in capProfits:
                return capProfits[capacity]

            totalProfit = helper(index+1, profit, weight, capacity)
            
            if weight[index] <= capacity:
                thisProfit = profit[index] + helper(index+1, profit, weight, capacity-weight[index])
                totalProfit = max(totalProfit, thisProfit)

            capProfits[capacity] = totalProfit
            return capProfits[capacity]

        retVal = helper(0, profit, weight, capacity)

        print(capProfits)

        return retVal
                    

