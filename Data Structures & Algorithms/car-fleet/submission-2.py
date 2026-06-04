from operator import itemgetter

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        pairs = sorted(pairs, key = itemgetter(0))
        pairs = pairs[::-1]
        stack = []
        for val in pairs:
            if not stack:
                time = (target - val[0]) / val[1]
                stack.append(time)
            else:
                time = (target - val[0]) / val[1]
                if stack[-1] < time:
                    stack.append(time)
        return len(stack)