class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for d, i in shift:
            if d == 0:
                s = s[i:] + s[:i]
            elif d == 1:
                s = s[-i:] + s[:-i]

        return s