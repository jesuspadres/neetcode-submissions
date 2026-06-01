class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retList = []
        self.helper(nums, [], retList, len(nums))

        return retList

    def helper(self, nums, permutation, retList, targetLen):
        if len(permutation) == targetLen:
            val = list(permutation)
            retList.append(val)
            return

        for i in range(len(nums)):
            permutation.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], permutation, retList, targetLen)
            permutation.pop(-1)
