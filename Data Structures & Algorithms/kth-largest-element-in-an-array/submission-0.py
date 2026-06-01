class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        retVal = 0
        for  i in range(k):
            retVal = heapq.heappop_max(nums)

        return retVal