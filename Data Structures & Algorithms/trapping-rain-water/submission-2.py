class Solution:
    def trap(self, heights: List[int]) -> int:
        maxL = heights[0]
        maxR = heights[-1]

        retVal = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            maxL = max(maxL, heights[l])
            maxR = max(maxR, heights[r])
            if maxL < maxR:
                retVal += max(0, maxL - heights[l])
                l += 1
            else:
                retVal += max(0, maxR - heights[r])
                r -= 1

        return retVal


        #################################### Solution 2 below


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