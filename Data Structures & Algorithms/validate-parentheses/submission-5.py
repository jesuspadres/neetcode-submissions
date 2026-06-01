class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "[{(":
                stack.append(c)
            else:
                if not stack:
                    return False
                openB = stack.pop()
                if c not in ")}]":
                    return False
                elif c == ")" and openB != "(":
                    return False
                elif c == "}" and openB != "{":
                    return False
                elif c == "]" and openB != "[":
                    return False

        return len(stack) == 0
