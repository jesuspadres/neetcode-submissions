class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        retVal = max(max(weights), sum(weights)//days)

        while True:

            count = 0
            time = 1
            for i,c in enumerate(weights):
                if count+c > retVal:
                    count = c
                    time += 1
                else:
                    count += c
            if time <= days:
                return retVal
            else:
                retVal += 1

        return -1
                    