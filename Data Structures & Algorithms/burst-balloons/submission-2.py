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

        r = helper(nums)
        print(cache)

        return r







        coins = 0
        print("coins: " + str(coins))

        for i in range(len(nums)):
            new_coins = 0
            baloon = 0
            for j in range(len(nums)):
                if j-1 < 0:
                    b0 = 1
                else:
                    b0 = nums[j-1]

                b1 = nums[j]

                try:
                    b2 = nums[j+1]
                except:
                    b2 = 1

                curr_coins = b0 * b1 * b2

                if j == len(nums)-1 and new_coins != 0:
                    break
                if b1 < nums[baloon] or new_coins == 0:
                    print(str(curr_coins) + " > " + str(new_coins))
                    print(str(b0) + " * " + str(b1) + " * " + str(b2) + " = " + str(curr_coins))
                    new_coins = curr_coins
                    baloon = j
                elif new_coins < curr_coins and baloon == 0:
                    new_coins = curr_coins
                    baloon = j


            coins += new_coins
            nums.pop(baloon)
            print("baloon popped: " + str(baloon))
            print("new coins added: " + str(new_coins))
            print("coins: " + str(coins) + "\n")

        return coins