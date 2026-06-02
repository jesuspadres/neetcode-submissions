class Solution:
    def customSortString(self, order: str, s: str) -> str:
        kvStoreNum = {}
        kvStoreChar = {}

        for i, n in enumerate(order):
            kvStoreNum[i] = n
            kvStoreChar[n] = i

        sNums = []

        i = 1
        for c in s:
            if c in kvStoreChar:
                sNums.append(kvStoreChar[c])
            else:
                kvStoreNum[i+26] = c
                kvStoreChar[c] = i+26
                sNums.append(i+26)
                i += 1

        sNums.sort()

        for i in range(len(sNums)):
            sNums[i] = kvStoreNum[sNums[i]]

        return "".join(sNums)

