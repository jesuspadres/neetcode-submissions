class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lists = []

        def recurse(currList, lists, nums):
            lists.append(list(currList))

            for i in range(len(nums)):
                currList.append(nums[i])
                recurse(currList, lists, nums[i+1:])
                currList.pop()

        recurse([], lists, nums)

        return lists