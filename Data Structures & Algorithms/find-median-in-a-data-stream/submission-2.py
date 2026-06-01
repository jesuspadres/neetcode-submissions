class MedianFinder:

    def __init__(self):
        self.lowerMaxPq = []
        self.upperMinPq = []

    def addNum(self, num: int) -> None:
        if not self.lowerMaxPq or self.lowerMaxPq[0] > num:
            heapq.heappush_max(self.lowerMaxPq, num)
        else:
            heapq.heappush(self.upperMinPq, num)

        lowerLen = len(self.lowerMaxPq)
        upperLen = len(self.upperMinPq)
        if lowerLen > upperLen + 1:
            heapq.heappush(self.upperMinPq, heapq.heappop_max(self.lowerMaxPq))
        elif upperLen > lowerLen + 1:
            heapq.heappush_max(self.lowerMaxPq, heapq.heappop(self.upperMinPq))

    def findMedian(self) -> float:
        lowerLen = len(self.lowerMaxPq)
        upperLen = len(self.upperMinPq)

        if lowerLen == upperLen:
            return (self.lowerMaxPq[0] + self.upperMinPq[0]) / 2
        elif lowerLen > upperLen:
            return self.lowerMaxPq[0]
        else:
            return self.upperMinPq[0]
        
        