class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        nums = set(nums)

        l2 = len(nums)

        return not l1 == l2