"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)
        start_times.sort()
        end_times.sort()
        result = 0
        count = 0
        start_pointer = 0
        end_pointer = 0
        while start_pointer < len(start_times):
            if start_times[start_pointer] < end_times[end_pointer]:
                start_pointer += 1
                count += 1
            else:
                end_pointer += 1
                count -= 1
            result = max(count, result)
        return result