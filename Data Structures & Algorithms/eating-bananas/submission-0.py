class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        retVal = r

        while l < r:
            mid = (l+r)//2
            time = 0

            for n in piles:
                time += math.ceil(n/mid)

            if time > h:
                l = mid+1
            else:
                retVal = min(retVal, mid)
                r = mid

        return retVal