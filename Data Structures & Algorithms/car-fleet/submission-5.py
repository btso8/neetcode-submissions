class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        stack = []
        for position, speed in pair:
            reach = (target - position) / speed
            stack.append(reach)
            while len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()
        return len(stack)