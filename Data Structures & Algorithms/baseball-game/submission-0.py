class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for operation in operations:
            if operation == "+":
                first_num = stack[-1]
                second_num = stack[-2]
                stack.append(first_num + second_num)
                result += first_num + second_num
            elif operation == "D":
                num = stack[-1]
                stack.append(num * 2)
                result += num * 2
            elif operation == "C":
                num = stack.pop()
                result -= num
            else:
                stack.append(int(operation))
                result += int(operation)
        return result