class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        cache = {}

        def helper(i):
            if i >= len(nums)-1:
                return True

            if i in cache:
                return cache[i]

            jumpVal = nums[i]
            valid = False
            for j in range(min(i+jumpVal, len(nums)-1), i, -1):
                if helper(j):
                    return True
                cache[j] = False

            cache[i] = False

            return False

        return helper(0)