class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retList = []

        l = 0
        r = k
        while r <= len(nums):
            retList.append(max(nums[l:r]))
            l += 1
            r += 1

        return retList