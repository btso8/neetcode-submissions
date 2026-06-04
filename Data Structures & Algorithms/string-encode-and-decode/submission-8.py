class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        strlength = ""
        while index < len(s):
            if s[index] == "#":
                result.append(s[index + 1 : index + int(strlength) + 1])
                index += int(strlength) + 1
                strlength = ""
            else:
                strlength += s[index]
                index += 1
        return result
