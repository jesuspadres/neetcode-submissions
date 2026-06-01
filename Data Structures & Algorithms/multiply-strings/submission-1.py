class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = []
        n2 = []

        for i in range(1, len(num1)+1):
            val = int(num1[-i])
            n1.append(pow(10, i-1)*val)

        for i in range(1, len(num2)+1):
            val = int(num2[-i])
            n2.append(pow(10, i-1)*val)

        n1Sum = 0
        for num in n1:
            n1Sum += num

        retVal = 0
        for num in n2:
            retVal += num * n1Sum

        retStr = ""

        while retVal > 0:
            val = retVal % 10
            retStr = str(val) + retStr
            retVal = retVal // 10

        return retStr