class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retList = [1]

        for i in range(len(nums)-1):
            retList.append(nums[i] * retList[i])

        postfix = 1
        for i in range(1, len(nums)+1):
            retList[-i] *= postfix
            postfix *= nums[-i]

        return retList