class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_hashmap = defaultdict(int)
        for num in nums:
            count_hashmap[num] += 1
        result = []
        for key, value in count_hashmap.items():
            if value > len(nums) // 3:
                result.append(key)
        return result