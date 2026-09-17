class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for val in paths:
            if val == "..":
                if stack:
                    stack.pop()
            elif val != "" and val != ".":
                stack.append(val)
        return "/" + "/".join(stack)