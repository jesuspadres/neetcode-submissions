class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removes = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ")":
                if not stack:
                    removes.append(i)
                else:
                    stack.pop()

        retVal = ""
        for i, c in enumerate(s):
            if i in stack or i in removes:
                continue
            retVal += c

        return retVal