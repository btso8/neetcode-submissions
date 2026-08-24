class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"[" : "]", "(" : ")", "{" : "}"}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if char != brackets[val]:
                    return False
        return not stack