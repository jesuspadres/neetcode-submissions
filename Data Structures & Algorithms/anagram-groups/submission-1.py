class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retList = []
        cache = {}
        
        for s in strs:
            abc = [0] * 26

            for c in s:
                abc[ord(c) - ord('a')] += 1

            key = ""
            for i in range(len(abc)):
                c = chr(ord('a') + i)
                val = abc[i]

                key += c + str(val)

            if key in cache:
                cache[key].append(s)
            else:
                cache[key] = [s]

        return list(cache.values())