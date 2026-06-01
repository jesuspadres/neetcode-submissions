class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {} # [(1,2)] = (piles,...)
        
        def helper(currPiles, turn, aStones, bStones):
            if not currPiles:
                if aStones > bStones:
                    return True
                return False

            tPiles = tuple(currPiles)
            if (aStones, bStones) not in cache:
                cache[(aStones, bStones)] = set()
            elif tPiles in cache[(aStones, bStones)]:
                return True

            winable = False

            if turn:
                o1 = helper(currPiles[1:], False, aStones + currPiles[0], bStones)
                if o1:
                    cache[(aStones, bStones)].add(tPiles)
                    return True
                o2 = helper(currPiles[:-1], False, aStones + currPiles[-1], bStones)

                winable = o1 or o2
            else:
                o1 = helper(currPiles[1:], True, aStones, bStones + currPiles[0])
                if o1:
                    cache[(aStones, bStones)].add(tPiles)
                    return True
                o2 = helper(currPiles[:-1], True, aStones, bStones + currPiles[-1])

                winable = o1 or o2

            if winable:
                cache[(aStones, bStones)].add(tPiles)

            return winable

        return helper(piles, True, 0, 0)


