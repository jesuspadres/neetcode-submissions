class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        for l in range(len(abbr)):
            if abbr[l].isnumeric():
                if abbr[l] == "0":
                    return False
                r = l+1
                while r < len(abbr) and abbr[r].isnumeric():
                    r += 1

                num = int(abbr[l:r])

                if l + num > len(word):
                    return False
                nextWord = word[l + num:]
                nextAbbr = abbr[r:]
                print(nextWord)
                print(nextAbbr)
                if self.validWordAbbreviation(nextWord, nextAbbr):
                    return True
                break
            elif l >= len(word) or abbr[l] != word[l]:
                return False

        

        return False

                
