# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        popularity = {}
        knower = {}
        for i in range(n):
            popularity[i] = 0
            knower[i] = 0

        for a in range(n):
            for b in range(n):
                if knows(a, b):
                    knower[a] += 1
                    popularity[b] += 1

        ignorants = []

        for i in range(n):
            if knower[i] == 1:
                ignorants.append(i)

        for i in ignorants:
            if popularity[i] == n:
                return i

        return -1
