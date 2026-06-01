class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        retVal = []
        added = False

        for pair in intervals:
            if added:
                retVal.append(pair)
                continue
            if pair[1] >= newInterval[0] and pair[0] <= newInterval[0]:
                newInterval[0] = min(pair[0], newInterval[0])
                newInterval[1] = max(pair[1], newInterval[1])
            elif pair[0] >= newInterval[0] and pair[0] <= newInterval[1]:
                newInterval[1] = max(pair[1], newInterval[1])
                newInterval[0] = min(pair[0], newInterval[0])
            else:
                if pair[0] > newInterval[0]:
                    retVal.append(newInterval)
                    added = True
                retVal.append(pair)

        if not added:
            retVal.append(newInterval)

        return retVal