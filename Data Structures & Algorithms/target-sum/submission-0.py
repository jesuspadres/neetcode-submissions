class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mapWays = {}
        retVal = 0

        def helper(i, count):
            nonlocal nums, target, mapWays

            if i > len(nums):
                return 0
            elif i == len(nums):
                return 1 if count == target else 0

            if (i, count) in mapWays:
                return mapWays[(i, count)]

            ways = helper(i+1, count+nums[i]) + helper(i+1, count-nums[i])
            mapWays[(i, count)] = ways

            return ways

        return helper(0,0)