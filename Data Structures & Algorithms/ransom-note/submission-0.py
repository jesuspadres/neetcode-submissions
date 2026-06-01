class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [0] * 26

        for c in magazine:
            i = ord(c) - ord("a")

            mag[i] += 1

        for c in ransomNote:
            i = ord(c) - ord("a")
            mag[i] -= 1

            if mag[i] < 0:
                return False

        return True
