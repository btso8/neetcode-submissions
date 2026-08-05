class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hashmap = defaultdict(int)
        for num in nums:
            count_hashmap[num] += 1
        frequency_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in count_hashmap.items():
            frequency_buckets[count].append(num)
        result = []
        for i in range(len(frequency_buckets) - 1, 0, -1):
            for num in frequency_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result