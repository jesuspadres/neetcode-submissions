class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        
        for s in strs:
            chars = [0] * 26

            for c in s:
                chars[ord(c) % 26] += 1

            tchars = tuple(chars)
            
            if tchars in map:
                map[tchars].append(s)
            else:
                map[tchars] = [s]

        retVal = []

        for v in map.values():
            retVal.append(v)

        return retVal
