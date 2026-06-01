class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        retList = [0] * len(temperatures)

        for i in range(len(retList) - 2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                retList[i] = 1
            else:
                j = i + 1
                while temperatures[j] <= temperatures[i]:
                    if retList[j] == 0:
                        j = i
                        break
                    j += retList[j]
                retList[i] = j-i

        return retList