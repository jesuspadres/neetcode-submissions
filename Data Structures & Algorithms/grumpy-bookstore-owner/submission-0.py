class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = list(grumpy)
        unsatisfied = list(grumpy)

        for i in range(len(grumpy)):
            if grumpy[i]:
                satisfied[i] = 0
                unsatisfied[i] = customers[i]
            else:
                satisfied[i] = customers[i]
                unsatisfied[i] = 0

        maxGrumpy = [0, minutes]
        grumpyCount = sum(unsatisfied[0:minutes])

        currCount = grumpyCount
        for i in range(len(grumpy)-minutes):
            currCount = currCount - unsatisfied[i] + unsatisfied[i+minutes]
            if currCount > grumpyCount:
                maxGrumpy = [i+1, i+minutes+1]
                grumpyCount = currCount

        retVal = 0
        print(satisfied, unsatisfied)

        for i in range(len(satisfied)):
            if i in range(maxGrumpy[0], maxGrumpy[1]):
                retVal += max(unsatisfied[i], satisfied[i])
            else:
                retVal += satisfied[i]

        return retVal
