class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                stackvalue, stackindex = stack.pop()
                result[stackindex] = index - stackindex
            stack.append([value, index])
        return result