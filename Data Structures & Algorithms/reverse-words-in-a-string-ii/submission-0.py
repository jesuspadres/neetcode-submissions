class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        word = "".join(s)

        sList = word.split()
        sList = sList[::-1]


        word = " ".join(sList)

        print(word)

        retVal = []

        for i, c in enumerate(word):
            print(c)
            s[i] = c

