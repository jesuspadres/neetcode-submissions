class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        retVal = heights[0]
        heights.append(0)

        stack = [[0, retVal]] # [index, height]

        for i in range(1, len(heights)):
            newIdx = i
            if heights[i] < heights[i-1]:
                while stack and heights[i] < stack[-1][1]:
                    index, height = stack.pop()
                    newIdx = index
                    retVal = max(retVal, (i-index) * height)
            stack.append([newIdx, heights[i]])

        return retVal
