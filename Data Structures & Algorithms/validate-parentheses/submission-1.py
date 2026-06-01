class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            elif stack == []:
                return False
            
            b = stack.pop()
            if b == '(' and c == ')':
                continue
            elif b == '{' and c == '}':
                continue
            elif b == '[' and c == ']':
                continue
            else:
                return False

        return stack == []
