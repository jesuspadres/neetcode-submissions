class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = set(coins)

        change = {}
        for i in range(1, amount+1):
            if i in coins:
                change[i] = 1
            else:
                currMin = 1000000
                for coin in coins:
                    if (i-coin) in change:
                        currMin = min(currMin, change[i-coin] + 1)

                if currMin != 1000000:
                    change[i] = currMin

        if amount not in change:
            return -1

        return change[amount]



