from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        rownums = defaultdict(set)
        colnums = defaultdict(set)
        boxnums = defaultdict(set)
        for r in range(size):
            for c in range(size):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rownums[r] or board[r][c] in colnums[c] or board[r][c] in boxnums[(r // 3, c // 3)]:
                    return False
                rownums[r].add(board[r][c])
                colnums[c].add(board[r][c])
                boxnums[(r // 3, c // 3)].add(board[r][c])
        return True