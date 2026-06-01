# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        a = 0
        for i in range(n):
            if knows(a, i):
                a = i

        celeb = True
        for b in range(n):
            if a == b:
                continue
            if knows(a, b) or not knows(b, a):
                celeb = False
        if celeb:
            return a
                    

        return -1
