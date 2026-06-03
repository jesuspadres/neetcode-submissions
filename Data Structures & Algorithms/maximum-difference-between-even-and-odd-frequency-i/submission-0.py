class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        maxOdd = None
        minEven = None

        for num in counts.values():
            if num % 2 == 1:
                if not maxOdd:
                    maxOdd = num
                else:
                    maxOdd = max(maxOdd, num)
            else:
                if not minEven:
                    minEven = num
                else:
                    minEven = min(minEven, num)

        return maxOdd - minEven