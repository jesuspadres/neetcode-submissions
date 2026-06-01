class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        s = set(nums)

        l2 = len(s)

        return not l1 == l2