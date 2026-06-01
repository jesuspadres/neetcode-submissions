class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        for i, c in enumerate(str(int("".join(digits))+1)):
            if i == len(digits):
                digits.append(int(c))
                return digits
            digits[i] = int(c)

        return digits

