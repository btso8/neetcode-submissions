class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True

    def search(self, word: str) -> bool:
        def dfs(start_index, current_root):
            current = current_root
            for i in range(start_index, len(word)):
                if word[i] == ".":
                    for value in current.children.values():
                        if dfs(i + 1, value):
                            return True
                    return False
                if word[i] not in current.children:
                    return False
                current = current.children[word[i]]
            return current.end

        return dfs(0, self.root)
