class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        if l == 3:
            return max(nums[0], nums[1], nums[2])

        nums2 = list(nums)
        nums[0] = 0
        nums2[-1] = 0

        lastLargest = nums[0]
        for i in range(2, l):
            nums[i] = max(nums[i] + lastLargest, nums[i-1], nums[i] + nums[i-2])
            lastLargest = max(nums[i-1], lastLargest)

        lastLargest = nums2[0]
        for i in range(2, l):
            nums2[i] = max(nums2[i] + lastLargest, nums2[i-1], nums2[i] + nums2[i-2])
            lastLargest = max(nums2[i-1], lastLargest)

        return max(nums[-1], nums2[-1])