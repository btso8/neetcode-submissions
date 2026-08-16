class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_hashmap = defaultdict(int)
        for num in nums:
            count_hashmap[num] += 1
            if len(count_hashmap) <= 2:
                continue
            new_count_hashmap = defaultdict(int)
            for num, count in count_hashmap.items():
                if count > 1:
                    new_count_hashmap[num] = count - 1
        result = []
        for num, count in count_hashmap.items():
            if count > len(nums) // 3:
                result.append(num)
        return result