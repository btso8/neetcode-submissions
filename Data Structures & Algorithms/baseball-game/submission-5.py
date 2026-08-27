class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []
        for val in operations:
            if val == "+":
                stack.append(stack[-1] + stack[-2])
                result += stack[-1]
            elif val == "D":
                stack.append(stack[-1] * 2)
                result += stack[-1]
            elif val == "C":
                num = stack.pop()
                result -= num
            else:
                result += int(val)
                stack.append(int(val))
        return result