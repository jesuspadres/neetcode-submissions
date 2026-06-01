class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        retLists = []
        nums.sort()

        def recurse(currList, nums, target, retLists):
            if not nums or target < 2:
                return

            for i, num in enumerate(nums):
                if num == target:
                    currList.append(num)
                    retLists.append(list(currList))
                    currList.pop()
                    return
                currList.append(num)
                recurse(currList, nums[i:], target - num, retLists)
                currList.pop()

        recurse([], nums, target, retLists)

        return retLists