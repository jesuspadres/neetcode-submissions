class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        maxVol = 0

        while l < r:
            minHeight = min(heights[l], heights[r])

            maxVol = max(maxVol, minHeight * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        l = 0
        r = len(heights) - 1
        while l < r:
            minHeight = min(heights[l], heights[r])

            maxVol = max(maxVol, minHeight * (r-l))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxVol


        