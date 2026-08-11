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
            current_index = index
            while s[current_index] != "#":
                current_index += 1
            length = int(s[index:current_index])
            index = current_index + 1
            current_index = index + length
            result.append(s[index:current_index])
            index = current_index
        return result