class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                current = board[row][col]
                if current == ".":
                    continue
                if current in rows[row] or current in cols[col] or current in squares[row // 3, col // 3]:
                    return False
                rows[row].add(current)
                cols[col].add(current)
                squares[row // 3, col // 3].add(current)
        return True