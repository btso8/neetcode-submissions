class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            word_index = index
            while s[word_index] != "#":
                word_index += 1
            word_size = int(s[index:word_index])
            index = word_index + 1
            word_index = index + word_size
            result.append(s[index:word_index])
            index = word_index
        return result