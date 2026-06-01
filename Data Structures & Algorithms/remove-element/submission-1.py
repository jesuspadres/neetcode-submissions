class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lastIdx = -1
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
            while nums[i] == val and lastIdx >= -len(nums):
                nums[i] = nums[lastIdx]
                lastIdx -= 1

        return k