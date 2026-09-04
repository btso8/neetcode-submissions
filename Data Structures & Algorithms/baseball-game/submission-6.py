class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
                result += stack[-1]
            elif o == "D":
                stack.append(stack[-1] * 2)
                result += stack[-1]
            elif o == "C":
                val = stack.pop()
                result -= val
            else:
                stack.append(int(o))
                result += int(o)
        return result