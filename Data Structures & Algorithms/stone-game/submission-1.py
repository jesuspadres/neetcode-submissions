class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a = set()
        b = set()
        
        def helper(currPiles, turn, aStones, bStones):
            if not currPiles:
                if aStones > bStones:
                    return True
                return False

            tPiles = tuple(currPiles)

            if tPiles in b or tPiles in a:
                return True

            winable = False

            if turn:
                o1 = helper(currPiles[1:], False, aStones + currPiles[0], bStones)
                o2 = helper(currPiles[:-1], False, aStones + currPiles[-1], bStones)

                winable = o1 or o2
                if winable:
                    a.add(tPiles)
            else:
                o1 = helper(currPiles[1:], True, aStones, bStones + currPiles[0])
                o2 = helper(currPiles[:-1], True, aStones, bStones + currPiles[-1])

                winable = o1 or o2
                if winable:
                    b.add(tPiles)

            return winable

        return helper(piles, True, 0, 0)


