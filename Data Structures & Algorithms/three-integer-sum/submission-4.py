class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = list()
        nums.sort()


        for i, n1 in enumerate(nums):
            if i > 0 and n1 == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums) - 1

            while j < k:
                n2 = nums[j]
                n3 = nums[k]
                if n1 + n2 + n3 == 0:
                    retList.append([n1, n2, n3])
                    j += 1
                    k -= 1
                    while nums[j] == n2 and j < k:
                        j += 1
                elif n1 + n2 + n3 < 0:
                    j += 1
                elif n1 + n2 + n3 > 0:
                    k -= 1

        return retList