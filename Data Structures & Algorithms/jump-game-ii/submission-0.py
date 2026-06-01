class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        count = 1
        valid = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= count:
                valid = i
            count += 1

        if valid == -1:
            return -1

        return 1 + self.jump(nums[:valid+1])