class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        index = 0
        result = []
        while index < len(s):
            current_index = index
            while s[current_index] != "#":
                current_index += 1
            size = int(s[index:current_index])
            index = current_index + 1
            current_index = index + size
            result.append(s[index:current_index])
            index = current_index
        return result