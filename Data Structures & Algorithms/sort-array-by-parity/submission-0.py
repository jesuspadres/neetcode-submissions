class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = len(nums)-1
        right = left

        while left >= 0:
            if nums[left] % 2 == 1:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                right -= 1

            left -= 1

        return nums