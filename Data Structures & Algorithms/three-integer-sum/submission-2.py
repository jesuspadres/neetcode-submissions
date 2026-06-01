class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = list()
        nums.sort()

        s = set()

        for i in range(len(nums)):
            n1 = nums[i]
            j = i+1
            k = len(nums) - 1

            while j < k:
                n2 = nums[j]
                n3 = nums[k]
                if n1 + n2 + n3 == 0 and (n1, n2) not in s:
                    retList.append([n1, n2, n3])
                    s.add((n1, n2))
                    j += 1
                    k -= 1
                elif n1 + n2 + n3 < 0:
                    j += 1
                elif n1 + n2 + n3 > 0:
                    k -= 1
                else:
                    j += 1
                    k -= 1

        return retList