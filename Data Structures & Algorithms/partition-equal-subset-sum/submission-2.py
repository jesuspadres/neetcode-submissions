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