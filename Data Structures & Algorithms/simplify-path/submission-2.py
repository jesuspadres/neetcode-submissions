class Solution:
    def simplifyPath(self, path: str) -> str:
        
        ops = path.split("/")

        stack = []

        for op in ops:
            if op == "..":
                if stack:
                    stack.pop()
            elif op == "" or op == ".":
                continue
            else:
                stack.append(op)

        if not stack:
            return "/"
        else:
            return "/" + "/".join(stack)