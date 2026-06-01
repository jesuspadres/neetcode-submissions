class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        sortedI = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                tmp = nums[sortedI]
                nums[sortedI] = nums[i]
                nums[i] = tmp
                sortedI += 1

        for i in range(sortedI, len(nums)):
            if nums[i] == 1:
                tmp = nums[sortedI]
                nums[sortedI] = nums[i]
                nums[i] = tmp
                sortedI += 1
