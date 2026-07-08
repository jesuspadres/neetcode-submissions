class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        leaderboard = sorted(counts.keys(), key= lambda x: counts[x], reverse= True)

        return leaderboard[:k]