class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def countW(word):
            c = Counter(word)

            return c["W"]

        retVal = k

        for i in range(len(blocks) - k + 1):
            retVal = min(retVal, countW(blocks[i:i+k]))

        return retVal