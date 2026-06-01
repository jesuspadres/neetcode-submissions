class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)

        retVal = 0

        minVal = min(s)
        maxVal = max(s)

        count = 0
        for i in range(minVal, minVal+1000):
            if i in s:
                count += 1

            if count > retVal:
                retVal = count

            if i not in s:
                count = 0

        count = 0
        for i in range(maxVal-1000, maxVal):
            if i in s:
                count += 1

            if count > retVal:
                retVal = count

            if i not in s:
                count = 0


        return retVal

