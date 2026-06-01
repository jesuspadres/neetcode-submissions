class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(subset, nums, retLists):
            if not nums:
                return

            subset.append(nums[0])
            if subset not in retLists:
                retLists.append(list(subset))

            helper(subset, nums[1:], retLists)
            subset.pop()
            helper(subset, nums[1:], retLists)

        retLists = [[]]
        helper([], nums, retLists)

        return retLists