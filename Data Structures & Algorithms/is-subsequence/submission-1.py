class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            return False

        count = 0

        for i in t:
            if count >= len(s):
                return True
            if i == s[count]:
                count += 1

        if count == len(s):
            return True
        else:
            return False