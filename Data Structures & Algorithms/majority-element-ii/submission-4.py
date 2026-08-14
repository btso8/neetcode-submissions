class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_hashmap = defaultdict(int)
        for num in nums:
            count_hashmap[num] += 1
        result = []
        for num, count in count_hashmap.items():
            if count > len(nums) // 3:
                result.append(num)
        return result