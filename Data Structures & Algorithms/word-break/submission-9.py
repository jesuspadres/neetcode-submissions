class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bads = set()

        def helper(s, wordDict):
            if not s or s == "":
                return True
            elif s in bads:
                return False
            wordDict = set(wordDict)

            for i in range(len(s), 0, -1):
                if s[:i] in wordDict:
                    rest = helper(s[i:], wordDict)
                    if rest:
                        return True
                    else:
                        bads.add(s[i:])

            return False

        return helper(s, wordDict)