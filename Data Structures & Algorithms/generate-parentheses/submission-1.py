class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(currVal, currOpen, currClosed, n, retList):
            if currOpen == n and currClosed == n:
                retList.append(currVal)

            if currOpen > currClosed:
                currVal += ")"
                currClosed += 1
                helper(currVal, currOpen, currClosed, n, retList)
                currVal = currVal[:-1]
                currClosed -= 1
            if currOpen < n:
                currVal += "("
                currOpen += 1
                helper(currVal, currOpen, currClosed, n, retList)
                currVal = currVal[:-1]
                currOpen -= 1

        retList = []
        helper("", 0, 0, n, retList)

        return retList