class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            difference = prefix - k
            if difference in prefix_sum:
                result += prefix_sum[difference]
            prefix_sum[prefix] += 1
        return result