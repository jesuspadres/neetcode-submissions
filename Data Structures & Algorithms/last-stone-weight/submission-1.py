class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x > y:
                res = x - y
                heapq.heappush_max(stones, res)
            

        if stones:
            return stones[0]

        return 0
