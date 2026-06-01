class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        retVal = 1

        def helper(subseqs, index):
            nonlocal retVal
            nonlocal nums

            if index >= len(nums):
                return 

            val = nums[index]
            newSubs = [[val]]
            for sub in subseqs:
                if val > sub[-1]:
                    sub2 = list(sub)
                    sub2.append(val)
                    newSubs.append(sub2)
                    retVal = max(retVal, len(sub2))
            subseqs += newSubs
            helper(subseqs, index+1)
                    
        helper([], 0)
        return retVal





