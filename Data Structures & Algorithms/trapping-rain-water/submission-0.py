class Solution:
    def trap(self, heights: List[int]) -> int:
        leftHeights = [0 for _ in heights]
        rightHeights = [0 for _ in heights]

        tallestLeft = 0
        tallestRight = 0
        for i in range(len(heights)):
            tallestLeft = max(tallestLeft, heights[i])
            leftHeights[i] = tallestLeft

            tallestRight = max(tallestRight, heights[-1-i])
            rightHeights[-i-1] = tallestRight

        retVal = 0

        for i in range(len(heights)):
            retVal += min(leftHeights[i], rightHeights[i]) - heights[i]

        return retVal