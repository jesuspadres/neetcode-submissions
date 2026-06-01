class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        retVal = 0
        
        prefixCount = {0:1}

        count = 0
        for i, c in enumerate(nums):
            count += c

            diff = count - k

            retVal += prefixCount.get(diff, 0)

            if count in prefixCount:
                prefixCount[count] += 1
            else:
                prefixCount[count] = 1

        return retVal