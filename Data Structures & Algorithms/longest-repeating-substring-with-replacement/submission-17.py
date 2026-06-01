class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        retVal = min(len(s), k)
        
        l = 0
        r = 1

        reps = k
        newL = r
        while l < len(s) and r < len(s):
            if s[l] == s[r]:
                retVal = max(retVal, r-l+1, r-l+1+reps)
            elif reps > 0:
                retVal = max(retVal, r-l+reps)
                if reps == k:
                    newL = r
                reps -= 1
            else:
                l = newL
                newL = l+1
                r = l
                reps = k

            r += 1

        s = s[::-1]
        l = 0
        r = 1

        reps = k
        newL = r
        while l < len(s) and r < len(s):
            if s[l] == s[r]:
                retVal = max(retVal, r-l+1, r-l+1+reps)
            elif reps > 0:
                retVal = max(retVal, r-l+reps)
                if reps == k:
                    newL = r
                reps -= 1
            else:
                l = newL
                newL = l+1
                r = l
                reps = k

            r += 1


        return min(retVal, len(s))
