class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            difference = prefix_sum - k
            if difference in prefix_sum_count:
                result += prefix_sum_count[difference]
            prefix_sum_count[prefix_sum] += 1
        return result