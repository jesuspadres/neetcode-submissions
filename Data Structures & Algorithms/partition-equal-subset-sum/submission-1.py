class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2
        retVal = False

        s = set()

        for num in nums:
            newSet = set()
            for val in s:
                newSet.add(num+val)
                newSet.add(val)
            s = newSet
            s.add(num)
            if half in s:
                return True

        return False




        def helper(currSum, i):
            nonlocal half, retVal, nums
            if currSum == half:
                retVal = True
            if i >= len(nums):
                return

            helper(currSum+nums[i], i+1)
            helper(currSum, i+1)

        helper(0, 0)

        return retVal