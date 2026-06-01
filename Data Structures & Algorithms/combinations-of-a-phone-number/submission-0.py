class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        retVal = []

        def helper(curr, nums):
            if not nums:
                if curr: retVal.append(curr)
                return

            d = int(nums[0])
            for c in dMap[d]:
                helper(curr+c, nums[1:])

        helper("", digits)

        return retVal 



