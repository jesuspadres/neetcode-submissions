class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for s in strings:
            key = ""
            diff = ord(s[0]) - ord('a')

            for c in s:
                asci = ord(c) - diff
                if asci < ord('a'):
                    asci += 26
                key += chr(asci)

            print(key)

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())