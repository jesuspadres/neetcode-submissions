class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        order = []
        apps = {}

        for i, c in enumerate(s):
            if c in apps:
                apps[c][1] = i
            else:
                apps[c] = [i, i]
                order.append(c)
                

        start = 0
        end = 1
        retList = []
        for i in range(1, len(order)):
            prev = apps[order[i-1]]
            curr = apps[order[i]]

            if prev[1] > curr[0] or end > curr[0]:
                end = max(end, prev[1], curr[1])
            else:
                retList.append(curr[0] - start)
                start = curr[0]

        retList.append(len(s) - start)

        return retList


# a [0, 8]
# b [1, 5]
