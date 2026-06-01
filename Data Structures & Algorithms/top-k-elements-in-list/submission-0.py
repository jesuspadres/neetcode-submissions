class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        leaderboard = [[] for _ in range(len(nums))]
        

        for key, v in map.items():
            leaderboard[v - 1] += [key]
            

        retList = []

        for i in range(1, len(leaderboard)+1):
            if k <= 0:
                break
            if len(leaderboard[-i]) > k:
                retList += leaderboard[-i][:k]
                break
            else:
                retList += leaderboard[-i]
                k -= len(leaderboard[-i])

        return retList

