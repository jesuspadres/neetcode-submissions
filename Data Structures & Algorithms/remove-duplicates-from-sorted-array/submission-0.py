class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        sorted = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[sorted-1]:
                nums[sorted] = nums[i]
                sorted += 1
                count += 1

        return count