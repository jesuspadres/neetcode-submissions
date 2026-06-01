class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def helper(currNums):
            if not currNums:
                return 0

            if tuple(currNums) in cache:
                return cache[tuple(currNums)]

            maxCoins = 0

            for i in range(len(currNums)):
                prev = 1
                if i-1 >= 0:
                    prev = currNums[i-1]
                post = 1
                if i+1 < len(currNums):
                    post = currNums[i+1]

                prod = prev*post*currNums[i] + helper(currNums[:i]+currNums[i+1:])

                maxCoins = max(maxCoins, prod)

            cache[tuple(currNums)] = maxCoins

            return maxCoins

        return helper(nums)

