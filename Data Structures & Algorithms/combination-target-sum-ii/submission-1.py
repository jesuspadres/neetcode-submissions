class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        retLists = []
        candidates.sort()

        def recurse(currList, nums, target, retLists):
            if not nums or target < 1:
                return

            for i, num in enumerate(nums):
                if num == target:
                    currList.append(num)
                    if currList not in retLists:
                        retLists.append(list(currList))
                    currList.pop()
                    return
                currList.append(num)
                recurse(currList, nums[i+1:], target - num, retLists)
                currList.pop()

        recurse([], candidates, target, retLists)

        return retLists