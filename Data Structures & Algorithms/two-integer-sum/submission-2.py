class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        retList = []

        cache = {}

        for i, num in enumerate(nums):
            dif = target - num
            if dif in cache:
                retList = [cache[dif], i]
                break
            else:
                cache[num] = i

        return retList