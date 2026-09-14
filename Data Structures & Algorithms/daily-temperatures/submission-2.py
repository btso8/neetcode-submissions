class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                t, i = stack.pop()
                result[i] = index - i
            stack.append((temperature, index))
        return result