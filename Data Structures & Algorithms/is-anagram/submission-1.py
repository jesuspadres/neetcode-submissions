class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        
        for c in s:
            chars[ord(c) % 26] += 1

        for c in t:
            chars[ord(c) % 26] -= 1

        for i in chars:
            if i != 0:
                return False

        return True