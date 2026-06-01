class Solution:
    def partition(self, s: str) -> List[List[str]]:
        retLists = []
        
        def isPalindrome(word):
            l = 0
            r = len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l+= 1
                r-= 1

            return True

        def helper(currList, currWord):
            if not currWord and currList:
                retLists.append(list(currList))

            for i in range(1, len(currWord)+1):
                pal = currWord[:i]
                if isPalindrome(pal):
                    print(pal)
                    currList.append(pal)
                    helper(currList, currWord[i:])
                    currList.pop()

        helper([], s)

        return retLists