class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0

        l = r = 0

        while l < len(chars):
            c = chars[l]

            while r < len(chars) and chars[r] == c:
                r += 1

            num = r - l
            l = r

            chars[pos] = c
            pos += 1
            
            if num > 1:
                num = str(num)
                for n in num:
                    chars[pos] = n
                    pos += 1

        return pos