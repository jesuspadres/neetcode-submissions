class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}

        for word in strs:
            alpha = [0 for _ in range(26)]

            for c in word:
                i = ord(c) - ord("a")

                alpha[i] += 1

            alpha = tuple(alpha)

            if alpha in cache:
                cache[alpha].append(word)
            else:
                cache[alpha] = [word]

        return list(cache.values())