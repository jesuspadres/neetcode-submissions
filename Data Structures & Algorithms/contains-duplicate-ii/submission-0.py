class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {} # number | how many times did it appear in the last k indices

        for i in range(len(nums)):
            num = nums[i]
            if i > k:
                cache[nums[i-k-1]] -= 1

            if num not in cache:
                cache[num] = 0

            if cache[num] > 0:
                return True

            cache[num] += 1 

        return False