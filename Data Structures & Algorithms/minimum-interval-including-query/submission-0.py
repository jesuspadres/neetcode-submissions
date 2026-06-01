class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        retList = []

        for q in queries:
            minDif = 100000
            for start, end in intervals:
                if q >= start and q <= end:
                    minDif = min(minDif, end - start + 1)
            if minDif == 100000:
                minDif = -1
            retList.append(minDif)


        return retList