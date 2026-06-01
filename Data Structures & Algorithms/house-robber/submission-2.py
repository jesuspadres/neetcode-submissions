class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prevMax = 0
        for i in range(2, len(nums)):
            nums[i] = max(nums[i]+nums[i-2], nums[i-1], nums[i]+prevMax)
            prevMax = max(nums[i-2], nums[i-1])

        return nums[-1]