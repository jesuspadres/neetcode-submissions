class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        for i in range(2, len(cost)):
            addition = min(cost[i-1], cost[i-2])
            cost[i] += addition

            if i+1 == len(cost):
                return min(cost[i], cost[i-1])

        return -1