class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = -k
        total = sum(cardPoints[right:])
        count = total

        for _ in range(k):
            
            count = count + cardPoints[left] - cardPoints[right]

            total = max(total, count)

            left += 1
            right += 1

        return total