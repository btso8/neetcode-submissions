class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        rows = len(board)
        columns = len(board[0])
        result = set()
        visit = set()
        def dfs(row, column, node, word):
            if (row < 0 or column < 0 or row == rows or column == columns or 
                (row, column) in visit or board[row][column] not in node.children):
                return
            visit.add((row, column))
            node = node.children[board[row][column]]
            word += board[row][column]
            if node.end:
                result.add(word)
            dfs(row - 1, column, node, word)
            dfs(row + 1, column, node, word)
            dfs(row, column - 1, node, word)
            dfs(row, column + 1, node, word)
            visit.remove((row, column))
        for row in range(rows):
            for column in range(columns):
                dfs(row, column, root, "")
        return list(result)