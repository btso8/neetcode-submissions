class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            difference = prefix - k
            if difference in prefix_counts:
                result += prefix_counts[difference]
            prefix_counts[prefix] += 1
        return result