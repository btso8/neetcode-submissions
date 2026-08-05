class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        result = []
        for num in nums:
            hashmap[num] += 1
        while k > 0:
            key = max(hashmap, key=hashmap.get)
            result.append(key)
            del hashmap[key]
            k -= 1
        return result