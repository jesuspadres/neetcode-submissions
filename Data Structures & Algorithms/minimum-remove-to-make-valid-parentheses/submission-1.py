class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s
        openStack = []
        closeStack = []

        retVal = ""

        for i, c in enumerate(s):
            if c == "(":
                openStack.append(i)
            elif c == ")":
                if openStack:
                    openStack.pop()
                else:
                    closeStack.append(i)

        openStack = set(openStack)
        closeStack = set(closeStack)
        
        for i, c in enumerate(s):
            if i not in openStack and i not in closeStack:
                retVal += c

        return retVal