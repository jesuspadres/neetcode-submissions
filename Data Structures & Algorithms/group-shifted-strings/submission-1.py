class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for s in strings:
            shift = ord(s[0]) - ord("a")

            key = ""

            for c in s:
                cVal = ord(c) - shift

                if cVal < ord("a"):
                    cVal += 26

                key += chr(cVal)

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())