class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def helper(si, pi):
            if (si, pi) in cache:
                return cache[(si, pi)]
            if si == len(s) and pi == len(p):
                return True
            if pi >= len(p):
                return False

            
            pVal = p[pi]
            wildcard = False
            if pi+1 < len(p) and p[pi+1] == "*":
                wildcard = True

            if si == len(s):
                if wildcard and pi+2 == len(p):
                    return True
                else:
                    return False
            sVal = s[si]
            match = False

            if sVal == pVal or pVal == ".":
                if wildcard:
                    match = match or helper(si+1, pi) or helper(si, pi+2) or helper(si+1, pi+2)
                else:
                    match = helper(si+1, pi+1)
            elif wildcard:
                match = match or helper(si, pi+2)

            cache[(si, pi)] = match

            return match

        return helper(0, 0)