class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        retVal = keyboard.index(word[0])

        
        for i in range(1, len(word)):
            prev = word[i-1]
            curr = word[i]

            retVal += abs(keyboard.index(prev) - keyboard.index(curr))

        return retVal

