class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = set()

        l = 0
        r = len(heights)-1

        while l < r:
            h1 = heights[l]
            h2 = heights[r]

            vol = min(h1, h2) * (r-l)

            water.add(vol)

            if h1 > h2:
                r -= 1
            else:
                l += 1

        return max(water)