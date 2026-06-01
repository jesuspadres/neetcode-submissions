class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = max(nums)
        if maxSum < 0:
            return maxSum
        currSum = 0

        for i in range(len(nums)):
            currSum = max(currSum + nums[i], 0)
            maxSum = max(maxSum, currSum)

        minSum = nums[0]
        currSum = 0
        totalSum = 0

        for i in range(len(nums)):
            totalSum += nums[i]
            currSum = min(currSum + nums[i], 0)
            minSum = min(minSum, currSum)

        return max(maxSum, totalSum - minSum)


