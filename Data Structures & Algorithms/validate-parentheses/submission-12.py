class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if not stack or brackets[stack.pop()] != bracket:
                    return False
        return not stack