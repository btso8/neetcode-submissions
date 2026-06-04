class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketpairs = {")" : "(", "]" : "[", "}" : "{"}
        for val in s:
            if val in bracketpairs:
                if stack and stack[-1] == bracketpairs[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        if stack:
            return False
        return True