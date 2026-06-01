class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        retVal = nums[0]
        count = 1

        for i in nums:
            if count <= 0:
                retVal = i
            elif i != retVal:
                count -= 1
            elif i == retVal:
                count += 1

        return retVal