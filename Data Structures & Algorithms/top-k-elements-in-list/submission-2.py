from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        result = []
        for num in nums:
            hashmap[num] += 1
        for key, value in hashmap.items():
            buckets[value].append(key)
        for bucket in range(len(buckets) - 1, 0, -1):
            for number in buckets[bucket]:
                result.append(number)
                if len(result) == k:
                    return result