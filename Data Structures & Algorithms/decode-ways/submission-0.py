class Solution:
    def numDecodings(self, s: str) -> int:
        retVal = 0
        
        def helper(string):
            nonlocal retVal
            if not string:
                return
            if len(string) == 1 and int(string) in range(1, 10):
                retVal += 1
                return
            if len(string) == 2 and int(string) in range(10, 27):
                retVal += 1

            s1 = int(string[0])
            s2 = int(string[:2])
            if s1 in range(1, 10):
                helper(string[1:])
            if s2 in range(10, 27):
                helper(helper(string[2:]))

        helper(s)

        return retVal

                
