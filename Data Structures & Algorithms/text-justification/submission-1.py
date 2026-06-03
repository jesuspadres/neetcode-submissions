class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def justifyReg(wordLine):
            nonlocal maxWidth

            lenWords = 0
            for word in wordLine:
                lenWords += len(word)

            spacer = (maxWidth - lenWords) // max(1, (len(wordLine) - 1))
            excess = (maxWidth - lenWords) % max(1, (len(wordLine) - 1))

            retVal = ""

            for i, w in enumerate(wordLine):
                if i == len(wordLine)-1:
                    retVal += w
                else:
                    retVal += w + (spacer * " ")

                    if excess > 0:
                        retVal += " "
                        excess -= 1

            return retVal

        def justifyLast(wordLine):
            nonlocal maxWidth

            retVal = " ".join(wordLine)

            retVal += " " * (maxWidth - len(retVal))

            return retVal

        wordLines = []
        wordLen = 0
        for i, word in enumerate(words):
            if not wordLines:
                wordLines.append([word])
                wordLen = len(word) + 1
            else:
                if wordLen + len(word) <= maxWidth:
                    wordLines[-1].append(word)
                    wordLen += len(word) + 1
                else:
                    wordLines.append([word])
                    wordLen = len(word) + 1

        retVal = []

        for i, wl in enumerate(wordLines):
            if i == len(wordLines)-1 or len(wl) == 1:
                retVal.append(justifyLast(wl))
            else:
                retVal.append(justifyReg(wl))

        return retVal











