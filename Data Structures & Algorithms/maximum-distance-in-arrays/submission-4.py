class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max1 = [arrays[0][0], 0]
        max2 = [arrays[1][0], 1]
        min1 = [arrays[0][0], 0]
        min2 = [arrays[1][0], 1]


        for i in range(len(arrays)):
            arr = arrays[i]

            arrMin = [min(arr), i]
            arrMax = [max(arr), i]

            if arrMax[0] > max2[0]:
                max2 = arrMax
            if arrMax[0] > max1[0]:
                max2 = max1
                max1 = arrMax

            if arrMin[0] < min2[0]:
                min2 = arrMin
            if arrMin[0] < min1[0]:
                min2 = min1
                min1 = arrMin

        print(max1, max2)
        print(min1, min2)

        if max1[1] != min1[1]:
            return abs(max1[0] - min1[0])
        else:
            retVal = float("-inf")
            if max1[1] != min2[1]:
                retVal = max(retVal, abs(max1[0] - min2[0]))
            if max2[1] != min1[1]:
                retVal = max(retVal, abs(max2[0] - min1[0]))
            if max2[1] != min2[1]:
                retVal = max(retVal, abs(max2[0] - min2[0]))

            return retVal



        