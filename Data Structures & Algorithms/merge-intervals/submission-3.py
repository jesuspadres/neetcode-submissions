class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)

        retList = []

        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            curr = intervals[i]

            if prev[1] >= curr[0]:
                curr[0] = prev[0]
                curr[1] = max(curr[1], prev[1])
                intervals[i] = curr
            else:
                retList.append(prev)

        retList.append(intervals[-1])

        return retList