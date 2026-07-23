class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        majority = len(nums) // 2
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > majority:
                return num