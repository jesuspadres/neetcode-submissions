class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        count = 0

        for i in s:
            if count >= len(t):
                return 0
            if i == t[count]:
                count += 1

        return len(t) - count