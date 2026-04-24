class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n= len(moves)
        left= moves.count('L')
        right= moves.count('R')
        blanks= moves.count('_')
        return abs(left-right)+blanks