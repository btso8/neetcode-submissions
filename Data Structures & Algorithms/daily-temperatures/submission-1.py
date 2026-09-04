class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                stack_value, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append([value, index])
        return result