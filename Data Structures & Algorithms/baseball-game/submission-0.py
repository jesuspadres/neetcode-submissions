class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for v in operations:
            if v == "+":
                num = s[-1] + s[-2]
                s.append(num)
            elif v == "D":
                num = s[-1] * 2
                s.append(num)
            elif v == "C":
                s.pop()
            else:
                s.append(int(v))

        return sum(s)