class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        length = len(s1)

        s1Alpha = [0] * 26
        s2Alpha = [0] * 26

        for c in s1:
            index = ord(c) - ord('a')
            s1Alpha[index] += 1

        for i in range(length):
            index = ord(s2[i]) - ord('a')
            s2Alpha[index] += 1

        for i in range(0, len(s2) - length + 1):
            if s1Alpha == s2Alpha:
                return True

            if i - 1 >= 0:
                index = ord(s2[i-1]) - ord('a')
                s2Alpha[index] -= 1

                index = ord(s2[i+length-1]) - ord('a')
                s2Alpha[index] += 1

        return s1Alpha == s2Alpha