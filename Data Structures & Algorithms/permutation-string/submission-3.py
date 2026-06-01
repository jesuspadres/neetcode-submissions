class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)

        l1 = sorted(s1)

        for i in range(0, len(s2) - length + 1):
            l2 = sorted(s2[i: i + length])

            print(l1, l2)
            if l1 == l2:
                return True

        return False