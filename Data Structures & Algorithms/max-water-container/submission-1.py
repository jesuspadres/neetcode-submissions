class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l = 0
        r = len(heights)-1

        while l < r:
            h1 = heights[l]
            h2 = heights[r]

            vol = min(h1, h2) * (r-l)

            maxWater = max(maxWater, vol)

            if h1 > h2:
                r -= 1
            else:
                l += 1

        return maxWater