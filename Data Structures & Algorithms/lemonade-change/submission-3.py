class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = 0
        change = {5 : 0, 10 : 0, 20 : 0}

        for bill in bills:
            print(change)
            if bill == 20:
                if change[5] > 0 and change[10] > 0:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
                change[20] += 1
            elif bill == 10 and change[5] > 0:
                change[5] -= 1
                change[10] += 1
            elif bill == 5:
                change[5] += 1
            else:
                return False

        return True