class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
                result += stack[-1]
            elif operation == "D":
                stack.append(stack[-1] * 2)
                result += stack[-1]
            elif operation == "C":
                val = stack.pop()
                result -= val
            else:
                stack.append(int(operation))
                result += int(operation)
        return result