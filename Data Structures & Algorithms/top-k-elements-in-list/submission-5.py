class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        frequency = []
        for _ in range(len(nums) + 1):
            frequency.append([])
        for num in nums:
            hashmap[num] += 1
        for num, count in hashmap.items():
            frequency[count].append(num)
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result