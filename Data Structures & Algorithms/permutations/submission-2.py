class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retList = []
        self.helper(nums, [], retList)

        return retList

    def helper(self, nums, permutation, retList):
        if not nums:
            retList.append(list(permutation))
            return

        for i in range(len(nums)):
            permutation.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], permutation, retList)
            permutation.pop()
