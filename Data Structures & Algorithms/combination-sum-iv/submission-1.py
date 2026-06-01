class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        cache[0] = 1

        def helper(currTarget):
            if currTarget in cache:
                return cache[currTarget]

            ways = 0

            for i in nums:
                if i <= currTarget:
                    ways += helper(currTarget - i)
            

            cache[currTarget] = ways
            return ways

        helper(target)


        return cache[target]