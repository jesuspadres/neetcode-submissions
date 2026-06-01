class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wLens = {}
        for word in words:
            wLens[word] = len(word)

        def helper(newWords):
            length = -1
            for word in newWords:
                length += 1 + wLens[word]

            if length <= maxWidth:
                return [" ".join(newWords) + (" " * (maxWidth-length))]

            if wLens[newWords[0]] == maxWidth:
                return [newWords[0]] + helper(newWords[1:])

            currSum = wLens[newWords[0]]
            spaces = 0
            index = 1
            for i in range(index, len(newWords)):
                spaces += 1
                if currSum + spaces + wLens[newWords[i]] <= maxWidth:
                    index += 1
                    currSum += wLens[newWords[i]]
                else:
                    break

            spaces = maxWidth - currSum

            newWord = ""

            for i in range(index-1, -1, -1):
                thisSpaces = 0
                if i != 0:
                    thisSpaces = spaces // (i)
                newWord = (" " * thisSpaces) + newWords[i] + newWord
                spaces -= thisSpaces

            return [newWord + (" " * (spaces))] + helper(newWords[index:])


        return helper(words)
        






#"a  b  c d"