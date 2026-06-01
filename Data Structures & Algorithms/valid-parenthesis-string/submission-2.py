class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        stars = 0

        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            elif c == "*":
                stars += 1
            if count < 0:
                stars += count
                count = 0
                if stars < 0:
                    return False

        count = 0
        stars = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == ")":
                count += 1
            elif c == "(":
                count -= 1
            elif c == "*":
                stars += 1
            if count < 0:
                stars += count
                count = 0
                if stars < 0:
                    return False

            
        return True

