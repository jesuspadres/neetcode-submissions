class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        currSum = maxSum
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]

            maxSum = max(maxSum, currSum)

        return maxSum