class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        d = {}

        for word1, word2 in similarPairs:
            d[word1] = d.get(word1, set())
            d[word1].add(word2)
            d[word2] = d.get(word2, set())
            d[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence2[i] in d and sentence1[i] in d[sentence2[i]]:
                continue
                
            return False

        return True
