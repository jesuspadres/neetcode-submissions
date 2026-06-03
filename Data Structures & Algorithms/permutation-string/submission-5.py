class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return True
        elif len(s1) > len(s2):
            return False

        s1Map = [0 for i in range(26)]
        s2Map = [0 for i in range(26)]

        for c in s1:
            s1Map[ord(c) - ord("a")] += 1

        l = len(s1)
        for i in range(l):
            s2Map[ord(s2[i]) - ord("a")] += 1

        if s1Map == s2Map:
            return True

        for i in range(1, len(s2) - l + 1):
            s2Map[ord(s2[i-1]) - ord("a")] -= 1
            s2Map[ord(s2[i-1+l]) - ord("a")] += 1

            if s1Map == s2Map:
                return True

        return False
            