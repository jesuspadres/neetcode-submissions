class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        winablePiles = {a : set(), b : set()}
        
        def helper(currPiles, turn, aStones, bStones):
            if not currPiles:
                if aStones > bStones:
                    return True
                return False

