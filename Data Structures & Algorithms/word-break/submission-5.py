class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        solus = set()
        bads = set()

        def helper(s, wordDict):
            if not s or s == "" or s in solus:
                return True
            elif s in bads:
                return False
            wordDict = set(wordDict)

            for i in range(len(s), 0, -1):
                if s[:i] in wordDict or s[:i] in solus:
                    solus.add(s[:i])
                    rest = helper(s[i:], wordDict)
                    if rest:
                        solus.add(s[i:])
                        return True
                    else:
                        bads.add(s[i:])

            return False

        return helper(s, wordDict)