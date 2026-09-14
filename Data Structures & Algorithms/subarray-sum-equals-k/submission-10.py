class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            difference = prefix_sum - k
            if difference in prefix_sum_counts:
                result += prefix_sum_counts[difference]
            prefix_sum_counts[prefix_sum] += 1
        return result
