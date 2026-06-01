class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []

        for val in path:
            if val == "" or val == ".":
                continue
            elif val == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(val)

        if not stack:
            return "/"

        retVal = ""

        for val in stack:
            retVal += "/" + val


        return retVal