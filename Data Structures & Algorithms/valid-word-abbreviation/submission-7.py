class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        aList = []

        tmp = ""
        for i in abbr:
            if i == "0" and tmp == "":
                return False
            if i.isnumeric():
                tmp += i
                continue
            elif tmp != "":
                aList.append(tmp)
                tmp = ""
            aList.append(i)
        if tmp != "":
            aList.append(tmp)
        print(aList)

        i = j = 0
        while i < len(word):
            if j >= len(aList):
                return False
            if word[i] == aList[j]:
                i += 1
                j += 1
            elif aList[j].isnumeric():
                i += int(aList[j])
                if i > len(word):
                    return False
                j += 1
            else:
                return False

        return j == len(aList)

