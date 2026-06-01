class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        highest = 0

        keyOccurence = {}
        keyValue = {}

        for num in nums:
            if num in keyValue:
                keyValue[num] += 1
            else:
                keyValue[num] = 1

            occurence = keyValue[num]
            highest = max(highest, occurence)

            if occurence > 1:
                keyOccurence[occurence-1].remove(num)

            if occurence in keyOccurence:
                keyOccurence[occurence].append(num)
            else:
                keyOccurence[occurence] = [num]

        
        retVal = []

        while highest > 0 and k > 0:
            arr = keyOccurence.get(highest, [])

            i = 0
            while k > 0 and i < len(arr):
                retVal.append(arr[i])
                i += 1
                k -= 1

            highest -= 1

        return retVal
