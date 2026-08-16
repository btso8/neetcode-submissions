class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0
        prefix = 0
        for num in nums:
            prefix += num
            difference = prefix - k
            if difference in prefix_count:
                result += prefix_count[difference]
            prefix_count[prefix] += 1
        return result