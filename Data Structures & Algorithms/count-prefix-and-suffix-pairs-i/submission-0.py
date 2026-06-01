class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        retVal = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                word1 = words[i]
                word2 = words[j]
                l1 = len(word1)
                l2 = len(word2)
                if l2 >= l1:
                    if word2[:l1] == word1 and word2[l2-l1:] == word1:
                        retVal += 1

        return retVal