class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}


        def helper(p1, p2, p3):
            if p3 >= len(s3):
                return True

            if (p1, p2, p3) in cache:
                return cache[(p1, p2, p3)]

            retVal = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                retVal = helper(p1+1, p2, p3+1)
            if p2 < len(s2) and s2[p2] == s3[p3]:
                retVal = retVal or helper(p1, p2+1, p3+1)

            cache[(p1, p2, p3)] = retVal

            return retVal

        return helper(0,0,0)

        