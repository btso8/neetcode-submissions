import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        answers = {}
        interval_index = 0
        for query in sorted(queries):
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                left, right = intervals[interval_index]
                interval_size = right - left + 1
                heapq.heappush(min_heap, (interval_size, right))
                interval_index += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            if min_heap:
                answers[query] = min_heap[0][0]
            else:
                answers[query] = -1
        result = []
        for query in queries:
            result.append(answers[query])
        return result