class StringIterator:
    

    def __init__(self, compressedString: str):
        self.fullString = ""
        self.index = 0

        s = compressedString
        l = r = 1
        while 0 < len(s):
            if s[r].isnumeric():
                r += 1
                if r < len(s):
                    continue
            num = int(s[l:r])
            self.fullString += num * s[0]
            s = s[r:]
            l = r = 1

            
 
    def next(self) -> str:
        if self.index < len(self.fullString):
            self.index += 1
            return self.fullString[self.index-1]

    def hasNext(self) -> bool:
        if self.index < len(self.fullString):
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
