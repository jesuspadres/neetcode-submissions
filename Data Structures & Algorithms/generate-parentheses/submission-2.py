class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        retList = []

        def helper(currVal, currOpen, currClosed):
            if currOpen == n == currClosed:
                retList.append(currVal)
                return

            if currOpen > currClosed:
                currVal += ")"
                helper(currVal, currOpen, currClosed+1)
                currVal = currVal[:-1]
            if currOpen < n:
                currVal += "("
                helper(currVal, currOpen+1, currClosed)
                currVal = currVal[:-1]

        
        helper("", 0, 0)

        return retList