class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()

        def explode(num: str):
            count = 0

            for d in num:
                d = int(d)

                count += d*d

            if count == 1:
                return True
            elif count in cycle:
                return False

            cycle.add(count)
            return explode(str(count))

        return explode(str(n))

            