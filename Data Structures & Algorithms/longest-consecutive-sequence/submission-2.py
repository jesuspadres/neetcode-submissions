class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0
        for num in numSet:
            maxLen = 1
            if num - 1 not in numSet:
                while num + maxLen in numSet:
                    maxLen += 1

            longest = max(maxLen, longest)

        return longest