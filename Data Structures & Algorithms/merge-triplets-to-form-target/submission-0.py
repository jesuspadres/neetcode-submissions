class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = False
        b = False
        c = False

        for x in triplets:
            xA = x[0]
            xB = x[1]
            xC = x[2]
            tA = target[0]
            tB = target[1]
            tC = target[2]

            if xA <= tA and xB <= tB and xC <= tC:
                if xA == tA:
                    a = True
                if xB == tB:
                    b = True
                if xC == tC:
                    c = True

        return a and b and c