class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
            else:
                output.append([interval[0], interval[1]])
        return output