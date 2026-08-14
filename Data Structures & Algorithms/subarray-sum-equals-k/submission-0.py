class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count_hashmap = defaultdict(int)
        prefix_sum_count_hashmap[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if prefix - k in prefix_sum_count_hashmap:
                result += prefix_sum_count_hashmap[prefix - k]
            prefix_sum_count_hashmap[prefix] += 1
        return result