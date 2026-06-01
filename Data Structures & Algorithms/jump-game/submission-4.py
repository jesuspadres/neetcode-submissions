class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0


        # DP (semi-greedy)

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